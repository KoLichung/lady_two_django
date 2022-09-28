from django.urls import path, include
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'), 
    path('register', views.register, name = 'register'), 
    path('member',views.member, name = 'member'),
    path('member_orders',views.member_orders, name = 'member_orders'),
    path('member_order_detail',views.member_order_detail, name = 'member_order_detail'), 
    path('products',views.products, name = 'products'),
    path('product_detail',views.product_detail, name = 'product_detail'),
    path('cart_order_list',views.cart_order_list, name = 'cart_order_list'),
    path('cart_payment_method',views.cart_payment_method, name = 'cart_payment_method'),
    path('cart_order_detail',views.cart_order_detail, name = 'cart_order_detail'),
    path('cart_order_confirmation',views.cart_order_confirmation, name = 'cart_order_confirmation'),
]