from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'backboard/login.html')

def products(request):
    return render(request, 'backboard/products.html')

def product_detail(request):
    return render(request, 'backboard/product_detail.html')

def orders(request):
    return render(request, 'backboard/orders.html')

def order_detail(request):
    return render(request, 'backboard/order_detail.html')

def customers(request):
    return render(request, 'backboard/customers.html')

def customer_detail(request):
    return render(request, 'backboard/customer_detail.html')

def bills(request):
    return render(request, 'backboard/bills.html')
