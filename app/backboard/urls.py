from django.urls import path, include
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('', views.login, name = 'login'),
    path('products', views.products, name = 'products'), 
    path('product_detail',views.product_detail, name = 'product_detail'),
    path('orders', views.orders, name = 'orders'), 
    path('order_detail',views.order_detail, name = 'order_detail'),
    path('customers', views.customers, name = 'customers'), 
    path('customer_detail',views.customer_detail, name = 'customer_detail'),
    path('bills',views.bills, name = 'bills'),
]