from ..models import Customer, Product
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from store.signals import order_created


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    """Create a new Customer automatically when a new new is created"""
    if kwargs["created"]:
        superuser = kwargs["instance"].is_superuser
        if not superuser:
            Customer.objects.create(user=kwargs["instance"])
            """Use this code to listen to fields and do what
            ever you want to do
            """


@receiver(order_created)
def reduce_product_quantity_on_order(sender, **kwargs):
    """Reduce the product quantity on order created"""
    product_quantity = kwargs["order"].inventory
    product_id = kwargs["order"].product.id
    old_quantity = Product.objects.only("inventory").get(id=product_id)
    new_quantity = old_quantity - product_quantity
    Product.objects.filter(pk=product_id).update(inventory=new_quantity)
