# This is the full code for mystore_project/stores/models.py

from django.db import models
from django.conf import settings 
from django.core.validators import MinValueValidator
import uuid 

# --- NEW THEME MODEL ---
class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    # Path to the preview image in static files, e.g., 'themes/eshopper/preview.png'
    preview_image = models.ImageField(upload_to='theme_previews/', blank=True, null=True)
    # The directory name where this theme's templates are stored
    # e.g., 'eshopper', 'moohaar_default'
    template_dir = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True) # So you can enable/disable themes

    def __str__(self):
        return self.name

class Store(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='stores'
    )
    # --- NEW FIELD ADDED TO STORE MODEL ---
    # Each store will have one theme. If the theme is deleted, set to NULL (or a default).
    active_theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, blank=True, null=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True) 
    business_email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    store_phone_number = models.CharField(max_length=20, blank=True, null=True)
    store_whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    
    # New address fields
    address = models.TextField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.name
    
    def clean(self):
        from django.core.exceptions import ValidationError
        # Ensure store name is not empty
        if not self.name or not self.name.strip():
            raise ValidationError('Store name cannot be empty.')
        
        # Ensure business email is valid if provided
        if self.business_email and '@' not in self.business_email:
            raise ValidationError('Please provide a valid business email address.')

class Product(models.Model):
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=60, blank=True, null=True, unique=False)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01, message="Price must be greater than 0")]
    )
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Weight in kg")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    stock_quantity = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0, message="Stock quantity cannot be negative")]
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['store', 'is_available']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name
    
    def clean(self):
        from django.core.exceptions import ValidationError
        # Ensure product name is not empty
        if not self.name or not self.name.strip():
            raise ValidationError('Product name cannot be empty.')
        
        # Ensure price is positive
        if self.price <= 0:
            raise ValidationError('Price must be greater than 0.')
        
        # Ensure stock quantity is not negative
        if self.stock_quantity < 0:
            raise ValidationError('Stock quantity cannot be negative.')
    
    def save(self, *args, **kwargs):
        # Auto-update availability based on stock
        if self.stock_quantity == 0:
            self.is_available = False
        elif self.stock_quantity > 0 and not self.is_available:
            self.is_available = True
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.name}"