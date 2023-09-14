from django import forms
from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm, PasswordChangeForm
from .models import Product, Order


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','category','image','image2','image3','image4','image5']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),

        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Company_Name','Address','delivery_address','delivery_port','email','Phone','products']
        widgets = {
            'Company_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_port': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'products': forms.Textarea(attrs={'class': 'form-control'}),

        }

