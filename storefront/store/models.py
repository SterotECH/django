from django.db import models
from django.utils.translation import gettext_lazy as _

# Many to Many RelationShip
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="+"
    )


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    inventory = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    class MemberChoices(models.TextChoices):
        MEMBERSHIP_EMPLOYEE = ("E", _("Employee"))
        MEMBERSHIP_ADMIN = ("A", _("Admin"))
        MEMBERSHIP_ROOT = ("R", _("Root"))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    date_of_birth = models.DateField(null=True)
    membership = models.CharField(
        max_length=1,
        choices=MemberChoices.choices,
        default=MemberChoices.MEMBERSHIP_EMPLOYEE,
    )


class Order(models.Model):
    PAYMENT_PENDING = "P"
    PAYMENT_COMPLETE = "C"
    PAYMENT_FAILED = "F"

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_COMPLETE, "Complete"),
        (PAYMENT_FAILED, "Failed"),
        (PAYMENT_PENDING, "Pending"),
    ]
    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_PENDING
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    # One-to-one Relationship
    # class Address (models.Model):
    #   street = models.CharField(max_length=255)
    #   city = models.CharField(max_length=255)
    #   customer = models.OneToOneField(Customer, on_delete=CASCADE, primary_key=True)

    # One-to-Many RelationShip
    # class Address(models.Model):
    #   street = models.CharField(max_length=255)
    #   city = models.CharField(max_length=255)
    #   customer = models.ForeignKey(Customer, on_delete=CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip = models.CharField(max_length=20)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
