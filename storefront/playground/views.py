from re import X
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F

from store.models import Product

# Create your views here.
# request -> respond
# request Handler
# actions


def say_hello(request):
    query_set = Product.objects.all()
    # Product Inventory < 10 AND price < 20
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    # Products: inventory = price
    # query_set = Product.objects.filter(inventory=F("unit_price"))

    # Sorting Data
    # query_set = Product.objects.order_by("unit_price", "-title").reverse()
    query_set = Product.objects.earliest("unit_price")
    return render(request, "hello.html", {"name": "Mosh", "products": list(query_set)})
