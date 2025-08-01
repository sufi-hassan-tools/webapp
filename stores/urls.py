from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('create/', views.create_store, name='create_store'),
    
    # Store Management URLs
    path('<uuid:store_id>/', views.store_detail, name='store_detail'),
    path('<uuid:store_id>/themes/', views.select_theme, name='select_theme'),
    path('<uuid:store_id>/themes/apply/', views.apply_theme, name='apply_theme'),
    path('<uuid:store_id>/theme/', views.theme_page, name='theme_page'),
    path('<uuid:store_id>/products/', views.product_list, name='product_list'),

    # Product Management URLs
    path('<uuid:store_id>/products/add/', views.add_product, name='add_product'),
    path('<uuid:store_id>/products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('<uuid:store_id>/products/<int:product_id>/delete/', views.delete_product, name='delete_product'),

    # API Endpoints
    path('api/store-profile/<uuid:profile_id>/', views.StoreProfileAPIView.as_view(), name='store_profile_api'),
    path('api/products/<uuid:store_id>/', views.ProductListAPIView.as_view(), name='product_list_api'),
]

