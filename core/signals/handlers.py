from store.signals import order_created
from django.dispatch import receiver


@receiver(order_created)
def on_order_created(sender, **kwargs):
    """Perform an action when an order is placed"""
    print(kwargs["order"])
