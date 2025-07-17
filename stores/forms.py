# This is the full code for mystore_project/stores/forms.py

from django import forms
from .models import Store, Product

class CustomClearableFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class StoreCreationForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'business_email', 'phone_number', 'whatsapp_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Store Name'}),
            'business_email': forms.EmailInput(attrs={'placeholder': 'Store Contact Email (Optional)'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Store Phone Number (Optional)'}),
            'whatsapp_number': forms.TextInput(attrs={'placeholder': 'Store WhatsApp Number (Optional)'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True


class ProductForm(forms.ModelForm):
    gallery_images = forms.FileField(
        required=False,
        widget=CustomClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'price', 'weight', 'description', 'stock_quantity', 'image', 'gallery_images']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'sku': forms.TextInput(attrs={'placeholder': 'SKU / Code'}),
            'category': forms.TextInput(attrs={'placeholder': 'Category'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your product', 'rows': 4}),
            'price': forms.NumberInput(attrs={'placeholder': '0.00'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'e.g., 0.5'}),
            'stock_quantity': forms.NumberInput(attrs={'placeholder': '0'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Example: Making description not strictly required by the form
        # (though the model allows blank=True, null=True)
        # self.fields['description'].required = False 
        # self.fields['image'].required = False # Model already allows blank=True for image
        pass # Add any other custom form initialization if needed
