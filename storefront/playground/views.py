from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.mail import EmailMessage, BadHeaderError
from store.models import Product

# Create your views here.
# request -> respond
# request Handler
# actions


def say_hello(request):
    try:
        message = EmailMessage('subject','message','from@sterobuy.com',['john@moshbuy.com'])
        message.attach_file('playground/static/images/dell-7Bmk9mAXP2I-unsplash.jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(
        request,
        "hello.html",
        {"name": "Mosh", },
    )
