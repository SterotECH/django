import logging
from urllib import response
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
# Create your views here.
# request -> respond
# request Handler
# actions

logger = logging.getLogger(__name__)


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            logger.info('Received the response')
            response = requests.get('https://httpbin.org/delay/2')
            data = response.json()
            return render(
                request, "hello.html", {"name": data},
            )
        except requests.ConnectionError:
            logger.critical('httpbin is offline')


# @cache_page(5 * 10)
# def say_hello(request):
