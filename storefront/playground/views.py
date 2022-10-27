from django.shortcuts import render
from django.http import HttpResponse
from .tasks import notify_customers
# Create your views here.
# request -> respond
# request Handler
# actions


def say_hello(request):
    notify_customers.delay('Hello')
    return render(
        request,
        "hello.html",
        {"name": "Mosh", },
    )
