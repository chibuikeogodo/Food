from django.shortcuts import render
from .models import Product
import random
# Create your views here.


def Home(request):
    products = Product.objects.all().order_by('-id')[:4]
    random_products = random.sample(list(products), 3)
    Vegetables = Product.objects.filter(category='Vegetables').order_by('-id')[:6]
    Oil = Product.objects.filter(category='Oil').order_by('-id')[:6]
    Fruits = Product.objects.filter(category='Fruits').order_by('-id')[:6]
    Grains = Product.objects.filter(category='Grains').order_by('-id')[:6]
    Dairy = Product.objects.filter(category='Dairy').order_by('-id')[:6]
    Protein = Product.objects.filter(category='Protein').order_by('-id')[:6]
    categories = [choice[0] for choice in Product.Categories]
    context = {
        'products': products,
        'random_products':random_products,
        'Vegetables': Vegetables,
        'Oil': Oil,
        'Fruits':Fruits,
        'Grains': Grains,
        'Dairy': Dairy,
        'Protein': Protein,
        'categories': categories
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'aboutUs.html')

def Products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product.html', context)