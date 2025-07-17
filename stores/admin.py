# This is the full code for mystore_project/stores/admin.py

from django.contrib import admin
from .models import Store, Product, Theme, ProductImage # Import Theme and ProductImage

# --- NEW: Admin configuration for the Theme model ---
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_dir', 'is_active')
    list_editable = ('is_active',)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'active_theme', 'created_at') # Added active_theme
    list_filter = ('user', 'created_at', 'active_theme')
    search_fields = ('name', 'user__email') 
    readonly_fields = ('id', 'created_at', 'updated_at') 

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'store', 'price', 'stock_quantity', 'is_available')
    list_filter = ('store', 'is_available', 'created_at')
    search_fields = ('name', 'store__name')
    list_editable = ('price', 'stock_quantity', 'is_available')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProductImageInline]

# Register all models
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
