from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage
from store.models import Product

# Create your views here.
# request -> respond
# request Handler
# actions


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='email/hello.html',
            context={'name':'Stero'},

            )
        message.send(['john@sterobuy.com'])
    except BadHeaderError:
        pass
    return render(
        request,
        "hello.html",
        {"name": "Mosh", },
    )
