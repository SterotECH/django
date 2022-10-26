from ..models import Customer
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    """Create a new Customer automatically when a new new is created"""
    if kwargs["created"]:
        print(kwargs["instance"].is_active)

        """Use this code to listen to fields and do what ever you want to do"""
        Customer.objects.create(user=kwargs["instance"])
