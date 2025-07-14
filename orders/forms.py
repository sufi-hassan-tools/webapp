# This is the full code for mystore_project/orders/forms.py

from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+92 300 1234567'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Street, G-9'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '44000'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Islamabad'}),
        }