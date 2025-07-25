from django import forms
from .models import Store, Product

class StoreCreationForm(forms.ModelForm):
    STATE_CHOICES = [
        ('', 'Select a Province/Territory'),
        ('AZAD JAMMU & KASHMIR', 'Azad Jammu & Kashmir'),
        ('BALOCHISTAN', 'Balochistan'),
        ('GILGIT-BALTISTAN', 'Gilgit-Baltistan'),
        ('ISLAMABAD CAPITAL TERRITORY', 'Islamabad Capital Territory'),
        ('KHYBER PAKHTUNKHWA', 'Khyber Pakhtunkhwa'),
        ('PUNJAB', 'Punjab'),
        ('SINDH', 'Sindh'),
    ]

    state = forms.ChoiceField(choices=STATE_CHOICES, required=True,
                              widget=forms.Select(attrs={'class': 'form-select'}))
    city = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    store_phone_number = forms.CharField(max_length=20, required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    store_whatsapp_number = forms.CharField(max_length=20, required=False,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Store
        fields = ['name', 'business_email', 'phone_number', 'whatsapp_number', 'state', 'city', 'address', 'store_phone_number', 'store_whatsapp_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'description', 'price', 'weight', 'image', 'stock_quantity', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
