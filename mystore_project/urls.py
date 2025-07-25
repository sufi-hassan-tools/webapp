# mystore_project/mystore_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from storefront.views import platform_home # Import the homepage view

urlpatterns = [
    # This line tells Django what to show at the root URL ('/')
    # Note: This view is also registered in storefront.urls with namespace for template references
    path('', platform_home, name='platform_home'), 
    
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('stores/', include('stores.urls')),
    path('shop/', include('storefront.urls')),
    path('dashboard/', TemplateView.as_view(template_name='base_react.html'), name='react_dashboard'),
]

# This part is for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)