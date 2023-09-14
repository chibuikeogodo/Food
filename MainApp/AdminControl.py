from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import auth, messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ProductForm
from .models import Product,Order
import random


def Dashbaord(request):
    products_count = Product.objects.all().count
    orders_count = Order.objects.all().count
    last_products = Product.objects.all().order_by('-id')[:1]
    last_order = Order.objects.all().order_by('-id')[:1]
    context = {
        'products_count':products_count,
        'orders_count':orders_count,
        'last_products':last_products,
        'last_order':last_order

    }
    return render(request, 'new/home.html',context)


def ProductList(request):
    products = Product.objects.all().order_by('-id')
    gadgets = Product.objects.filter(category='Gadgets')
    panels = Product.objects.filter(category='Panels')
    Drones = Product.objects.filter(category='Drones')
    Batteries = Product.objects.filter(category='Batteries')
    home = Product.objects.filter(category='Home Appliances')
    auto = Product.objects.filter(category='Electric Autos')
    categories = [choice[1] for choice in Product.Categories]
    context = {
        'products': products,
        'gadgets': gadgets,
        'Drones':Drones,
        'Batteries':Batteries,
        'home':home,
        'auto':auto,
        'panels':panels,
        'categories': categories
    }
    return render(request, 'products/admin-product.html', context)

def Products(request):
    products = Product.objects.all()
    gadgets = Product.objects.filter(category='Gadgets')
    Drones = Product.objects.filter(category='Drones')
    Batteries = Product.objects.filter(category='Batteries')
    home = Product.objects.filter(category='Home Appliances')
    auto = Product.objects.filter(category='Electric Autos')
    categories = [choice[1] for choice in Product.Categories]
    context = {
        'products': products,
        'gadgets': gadgets,
        'Drones':Drones,
        'Batteries':Batteries,
        'home':home,
        'auto':auto,
        'categories': categories
    }
    return render(request, 'products/admin-product.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProductList')
    else:
        form = ProductForm()
    return render(request, 'products/add-product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ProductList')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update-product.html', {'form': form})

def delete_products(request, pk):
    category = Product.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('ProductList')
    return render(request, 'products/delete-products.html', {'category': category})

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product-details.html', {'product': product})