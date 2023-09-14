import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import random


class Product(models.Model):
    Categories = (
        ('Vegetables', 'Vegetables'),
        ('Oil', 'Oil'),
        ('Fruits', 'Fruits'),
        ('Grains', 'Grains'),
        ('Dairy', 'Dairy'),
        ('Protein', 'Protein')

    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, default=None)
    image2 = models.ImageField(null=True, blank=True, default=None)
    image3 = models.ImageField(null=True, blank=True, default=None)
    image4 = models.ImageField(null=True, blank=True, default=None)
    image5 = models.ImageField(null=True, blank=True, default=None)
    category = models.CharField(max_length=30, choices=Categories)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Company_Name = models.CharField(max_length=300, default=None)
    Address = models.CharField(max_length=300, default=None)
    delivery_address = models.CharField(max_length=300, default=None)
    delivery_port = models.CharField(max_length=300, default=None)
    products = models.TextField()
    email = models.CharField(max_length=300, default=None)
    Phone = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    order_number = models.PositiveIntegerField(unique=True, editable=False, default=None)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_unique_order_number()
        super().save(*args, **kwargs)

    def generate_unique_order_number(self):
        while True:
            order_number = random.randint(100000, 999999)
            if not Order.objects.filter(order_number=order_number).exists():
                return order_number

    def __str__(self):
        return f"Order #{self.pk} - User: {self.user.username}"
