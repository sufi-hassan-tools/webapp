# mystore_project/stores/urls.py

from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('create/', views.create_store, name='create_store'),
    
    # Store Management URLs
    path('<uuid:store_id>/', views.store_detail, name='store_detail'),
    path('<uuid:store_id>/themes/', views.select_theme, name='select_theme'),
    path('<uuid:store_id>/themes/apply/', views.apply_theme, name='apply_theme'),
    path('<uuid:store_id>/products/', views.product_list, name='product_list'), # <-- NEW URL

    # Product Management URLs
    path('<uuid:store_id>/products/add/', views.add_product, name='add_product'),
    path('<uuid:store_id>/products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('<uuid:store_id>/products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
]