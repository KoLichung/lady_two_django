from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

def register(request):
    return render(request, 'web/register.html')

def member(request):
    return render(request, 'web/member.html')

def member_orders(request):
    return render(request, 'web/member_orders.html')

def member_order_detail(request):
    return render(request, 'web/member_order_detail.html')

def products(request):
    return render(request, 'web/products.html')

def product_detail(request):
    return render(request, 'web/product_detail.html')

def cart_order_list(request):
    return render(request, 'web/cart_order_list.html')

def cart_payment_method(request):
    return render(request, 'web/cart_payment_method.html')

def cart_order_detail(request):
    return render(request, 'web/cart_order_detail.html')

def cart_order_confirmation(request):
    return render(request, 'web/cart_order_confirmation.html')