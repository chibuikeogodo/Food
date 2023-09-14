from django.contrib import admin
from django.urls import path, include
from .views import Home, Products,about
from .orders import create_order,orders,order_detail,UserOrderListView,UserOrderDetailView
from .AdminControl import Dashbaord,ProductList,update_product,delete_products,create_product,product_detail
from .Account import Login, register,logout
urlpatterns = [
    path('', Home, name='Home'),
    path('about-us', about, name='about'),
    path('Products', Products, name='Products'),
    path('Login', Login, name='Login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('Dashbaord', Dashbaord, name='Dashbaord'),
    path('ProductList', ProductList, name='ProductList'),
    path('add-new-product',create_product, name='create_product'),
    path('products/update/<int:pk>', update_product, name='update_product'),
    path('products/delete/<int:pk>',delete_products, name='delete_products'),
    path('product/<slug:product_slug>/', product_detail, name='product_detail'),
    path('create_order', create_order, name='create_order'),
    path('orders', orders, name='orders'),
    path('order_detail/<int:id>/', order_detail, name='order_detail'),
    path('user/orders/', UserOrderListView.as_view(), name='user-orders'),
    path('user/orders/<int:pk>/', UserOrderDetailView.as_view(), name='user-order-detail'),
]
