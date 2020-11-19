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
  
  total_customers = customers.count()
  
  total_orders = orders.count()
  delivered = orders.filter(status='Delivered').count()
  pending = orders.filter(status='Pending').count()
  
  context = {'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
  
  return render(request, 'accounts/dashboard.html', context)

def products(request):
  products = Product.objects.all()
  return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
  customer = Customer.objects.get(id=pk)
  
  orders = customer.order_set.all()
  total_orders = orders.count()
  
  context = {'customer': customer, 'orders': orders, 'total_orders': total_orders}
  return render(request, 'accounts/customer.html', context)

# once you create your views import them into the urls.py file you created in this same directory

