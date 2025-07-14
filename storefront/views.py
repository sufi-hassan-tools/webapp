# mystore_project/storefront/views.py

from django.shortcuts import render, get_object_or_404
from stores.models import Store, Product 

# --- ADD THIS NEW VIEW ---
def platform_home(request):
    """
    The main landing page for the Moohaar platform itself.
    """
    return render(request, 'storefront/platform_home.html')
# --- END OF NEW VIEW ---


def store_home(request, store_id):
    """ The public-facing homepage for an individual store. """
    store = get_object_or_404(Store, id=store_id)
    products = Product.objects.filter(store=store, is_available=True)
    
    context = { 'store': store, 'products': products[:8] }
    
    template_path = f'themes/{store.active_theme.template_dir}/index.html'
    return render(request, template_path, context)


def product_detail(request, store_id, product_id):
    """ The public-facing detail page for a single product. """
    store = get_object_or_404(Store, id=store_id)
    product = get_object_or_404(Product, id=product_id, store=store, is_available=True)
    
    context = { 'store': store, 'product': product }
    
    template_path = f'themes/{store.active_theme.template_dir}/detail.html'
    return render(request, template_path, context)