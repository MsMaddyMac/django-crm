from django.shortcuts import render
from django.http import HttpResponse

# Create your views (pages) here.
def home(request):
  return HttpResponse('home')

def products(request):
  return HttpResponse('products')

def customer(request):
  return HttpResponse('customer')

# once you create your views import them into the urls.py file you created in this same directory

