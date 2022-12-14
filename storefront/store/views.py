from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.viewsets import GenericViewSet, ModelViewSet

from store.pagination import DefaultPagination
from store.permissions import IsAdminOrReadOnly, ViewCustomerHistoryPermission

from .filters import ProductFilter
from .models import (
    Cart,
    CartItem,
    Collection,
    Customer,
    Order,
    OrderItem,
    Product,
    ProductImage,
    Review,
)
from .serializer import (
    AddCartItemSerializer,
    CartItemSerializer,
    CartSerializer,
    CollectionSerializer,
    CreateOrderSerializer,
    CustomerSerializer,
    OrderItemSerializer,
    OrderSerializer,
    ProductImageSerializer,
    ProductSerializer,
    ReviewSerializer,
    UpdateCartItemSerializer,
    UpdateOrderSerializer,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('images').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ["title", "description"]
    ordering_fields = ["title", "unit_price", "last_update"]

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count() > 0:
            return Response(
                {
                    "error": "Product cannot be deleted because it \
                        is associated with an order item"
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count("products"),
    ).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs["pk"]).count() > 0:

            return Response(
                {
                    "error": "Collection cannot be \
                        deleted as it contains products",
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["product_pk"])

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}


class CartViewSet(
    CreateModelMixin,
    GenericViewSet,
    RetrieveModelMixin,
    DestroyModelMixin,
):
    serializer_class = CartSerializer
    queryset = Cart.objects.prefetch_related("items__product").all()


class CartItemViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        if self.request.method == "PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(
            cart_id=self.kwargs["cart_pk"],
        ).select_related("product")

    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response("OK")

    @action(
        detail=False,
        methods=["GET", "PUT"],
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        customer = Customer.objects.get(
            user_id=request.user.id,
        )
        if request.method == "GET":
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = CustomerSerializer(customer, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = CartItem.objects.select_related("items__order_items").all()


class OrderViewSet(ModelViewSet):
    http_method_names = ["get", "patch", "delete", "post", "head", "options"]

    def get_permissions(self):
        if self.request.method in ["PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data=request.data,
            context={"user_id": self.request.user.id},  # type: ignore
        )
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return UpdateOrderSerializer
        elif self.request.method == "POST":
            return CreateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # type: ignore
            return Order.objects.all()
        customer_id = Customer.objects.only("id").get(
            user_id=user.id,  # type: ignore
        )
        Order.objects.filter(customer_id=customer_id)


class ProductImageViewSet(ModelViewSet):
    """Manage the product image endpoint"""

    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(
            product_id=self.kwargs["product_pk"],
        )

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}
