from django.urls import path
from . import views

app_name = 'storefront'

urlpatterns = [
    # Add the platform homepage URL here as well, so it can be referenced as 'storefront:platform_home'
    path('platform-home/', views.platform_home, name='platform_home'),
    
    # URLs for a specific store's public-facing pages
    path('<uuid:store_id>/', views.store_home, name='store_home'),
    path('<uuid:store_id>/product/<int:product_id>/', views.product_detail, name='product_detail'),
]