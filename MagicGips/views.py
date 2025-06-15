from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(request, 'MagicGips/products/products.html')

def products(request):
    return render(request, 'MagicGips/products/products.html')

def product_detail(request, product_name):
    template_name = f'MagicGips/products/{product_name}.html'
    return render(request, template_name)