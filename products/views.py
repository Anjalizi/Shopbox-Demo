from django.shortcuts import render
from .models import Product

def index(request):
	return render(request, 'products/index.html')

def all_products(request):
	products = Product.objects.all()
	return render(request, 'products/all_products.html', {'all_products':products})
