from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views (pages) here.
# this is a view which will show the string passed into the HttpResponse() when someone visits that particular page(view)
# def home(request):
#   return HttpResponse('home')

# this is what the def changes to if you have a template to render on that page(view)
# you point it to the file path of the template within the templates directory. In this case within the templates directory there is an accounts directory and within that a dashboard.html file
def home(request):
  orders = Order.objects.all()
  customers = Customer.objects.all()
  print('customers', customers)
  
  context = {'orders': orders, 'customers': customers}
  
  return render(request, 'accounts/dashboard.html', context)

def products(request):
  products = Product.objects.all()
  return render(request, 'accounts/products.html', {'products': products})

def customer(request):
  return render(request, 'accounts/customer.html')

# once you create your views import them into the urls.py file you created in this same directory

