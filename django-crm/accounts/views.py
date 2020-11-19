from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
# flash message
from django.contrib import messages

from .models import *
from .forms import *
from .filters import OrderFilter

# Create your views (pages) here.
# this is a view which will show the string passed into the HttpResponse() when someone visits that particular page(view)
# def home(request):
#   return HttpResponse('home')

# this is what the def changes to if you have a template to render on that page(view)
# you point it to the file path of the template within the templates directory. In this case within the templates directory there is an accounts directory and within that a dashboard.html file
def registerPage(request):
  form = CreateUserForm()
  
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request, 'Account was created for ' + user)
      
      return redirect('login')
      
  context = {'form': form}
  return render(request, 'accounts/register.html', context)

def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request, 'Username OR password is incorrect!')
      
  context = {}
  return render(request, 'accounts/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')

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
  
  myFilter = OrderFilter(request.GET, queryset=orders)
  orders = myFilter.qs
  
  context = {'customer': customer, 'orders': orders, 'total_orders': total_orders, 'myFilter': myFilter}
  return render(request, 'accounts/customer.html', context)

def createOrder(request, pk):
  OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
  customer = Customer.objects.get(id=pk)
  formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
  
  # form = OrderForm(initial={'customer': customer})
  if request.method == 'POST':
    # print('printing POST:', request.POST)
    # form = OrderForm(request.POST)
    formset = OrderFormSet(request.POST, instance=customer)
    if formset.is_valid():
      formset.save()
      return redirect('/')
    
  context = {'formset': formset}
  return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
  order = Order.objects.get(id=pk)
  form = OrderForm(instance=order)
  
  if request.method == 'POST':
    form = OrderForm(request.POST, instance=order)
    if form.is_valid():
      form.save()
      return redirect('/')
    
  context = {'form': form}
  return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
  order = Order.objects.get(id=pk)
  if request.method == 'POST':
    order.delete()
    return redirect('/')
  
  context = {'order': order}
  return render(request, 'accounts/delete.html', context)

# once you create your views import them into the urls.py file you created in this same directory

