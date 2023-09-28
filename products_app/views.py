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

def profil_page(request):
    return render(request, 'profile.html')

def buyurtma_page(request):
    return render(request, 'buyurtmalar.html')

def category_page(request, cat_id):
    product = Product.objects.filter(category=cat_id)
    category = ProductCategory.objects.all()
    context = {
        "products": product,
        "categories": category
    }
    return render(request, 'products.html', context)