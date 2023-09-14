from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import auth, messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ProductForm,OrderForm
from .models import Product, Order


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Assign the logged-in user as the 'name'
            order.save()
            return redirect('user-orders')  # Redirect to a list view of orders
    else:
        form = OrderForm()

    context = {'form': form}
    return render(request, 'orders/order-product.html', context)


def orders(request):
    orders = Order.objects.all().order_by('-id')
    context = {
        'orders': orders,

    }
    return render(request, 'orders/order-list.html', context)

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

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'orders/order-details.html', {'order': order})

class UserOrderListView(LoginRequiredMixin, View):
    template_name = 'orders/user-order.html'  # Create this template

    def get(self, request, *args, **kwargs):
        user_orders = Order.objects.filter(user=request.user).order_by('-date')
        context = {'user_orders': user_orders}
        return render(request, self.template_name, context)

class UserOrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/user-order-details.html'  # Create this template

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

