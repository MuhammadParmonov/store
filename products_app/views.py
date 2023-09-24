from django.shortcuts import render

from .models import ProductCategory, Product


def index_view(request):
    context = {
        "title": "Store"
    }
    return render(request, 'index.html', context)

def product_view(request):
    category = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        "title": "Store - Каталог",
        "categories": category,
        "products": products
    }
    return render(request, 'products.html', context)