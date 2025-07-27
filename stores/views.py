from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from django.core.paginator import Paginator

from .forms import StoreCreationForm, ProductForm
from .models import StoreProfile, Product, Store, Theme
from .serializers import StoreProfileSerializer, ProductSerializer

# Store creation view
def create_store(request):
    """Create a new store for the logged in user."""
    if request.method == 'POST':
        form = StoreCreationForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.user = request.user
            store.save()
            return redirect('stores:store_detail', store_id=store.id)
    else:
        form = StoreCreationForm()
    return render(request, 'stores/create_store.html', {'form': form})

# API Views
class StoreProfileAPIView(generics.RetrieveAPIView):
    queryset = StoreProfile.objects.all()
    serializer_class = StoreProfileSerializer
    lookup_field = 'profile_id' # Assuming profile_id is unique for lookup

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        store_id = self.kwargs['store_id']
        return Product.objects.filter(store__id=store_id)


def store_detail(request, store_id):
    """Display details for a single store with its products."""
    store = get_object_or_404(Store, id=store_id)
    products = Product.objects.filter(store=store)
    return render(request, 'stores/store_detail.html', {
        'store': store,
        'products': products,
    })


# New view for selecting a store theme
def select_theme(request, store_id):
    """Display a page to choose a theme for the given store."""
    store = get_object_or_404(Store, id=store_id)
    themes = Theme.objects.filter(is_active=True)
    return render(request, 'stores/select_theme.html', {
        'store': store,
        'themes': themes,
    })


def apply_theme(request, store_id):
    """Apply the selected theme to the store."""
    store = get_object_or_404(Store, id=store_id)
    if request.method == 'POST':
        theme_id = request.POST.get('theme_id')
        if theme_id:
            theme = get_object_or_404(Theme, id=theme_id)
            store.active_theme = theme
            store.save()
            return render(request, 'stores/theme_applied.html', {
                'store': store,
                'theme': theme,
            })
    themes = Theme.objects.filter(is_active=True)
    return render(request, 'stores/apply_theme.html', {
        'store': store,
        'themes': themes,
    })


def theme_page(request, store_id):
    """Display the store theme settings page."""
    store = get_object_or_404(Store, id=store_id)
    return render(request, 'stores/theme_page.html', {'store': store})


def product_list(request, store_id):
    """List products for a store with optional search and pagination."""
    store = get_object_or_404(Store, id=store_id)
    products = Product.objects.filter(store=store)
    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(name__icontains=search_query)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    context = {
        'store': store,
        'products': products_page,
        'search_query': search_query,
    }
    return render(request, 'stores/product_list.html', context)


def add_product(request, store_id):
    """Add a product to the store."""
    store = get_object_or_404(Store, id=store_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            return redirect('stores:product_list', store_id=store.id)
    else:
        form = ProductForm()
    context = {
        'store': store,
        'form': form,
        'page_title': 'Add Product',
    }
    return render(request, 'stores/product_form.html', context)


def edit_product(request, store_id, product_id):
    """Edit an existing product."""
    store = get_object_or_404(Store, id=store_id)
    product = get_object_or_404(Product, id=product_id, store=store)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('stores:product_list', store_id=store.id)
    else:
        form = ProductForm(instance=product)
    context = {
        'store': store,
        'form': form,
        'product': product,
        'page_title': 'Edit Product',
    }
    return render(request, 'stores/product_form.html', context)


def delete_product(request, store_id, product_id):
    """Delete a product from the store."""
    store = get_object_or_404(Store, id=store_id)
    product = get_object_or_404(Product, id=product_id, store=store)
    if request.method == 'POST':
        product.delete()
        return redirect('stores:product_list', store_id=store.id)
    return render(request, 'stores/product_confirm_delete.html', {
        'store': store,
        'product': product,
    })


