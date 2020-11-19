from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/<str:pk>/', views.customer),
]

# once you create paths for views include them in the urls.py of the main app 'crm app'
