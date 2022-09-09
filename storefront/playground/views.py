
from re import X
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> respond 
# request Handler 
# actions 
def calculate():
  x=10
  y=6
  return x 

def say_hello(request):
  x = calculate()
  return render(request,'hello.html', {'name':"Mosh"})
  