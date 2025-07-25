# mystore_project/stores/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import StoreCreationForm, ProductForm 
from .models import Store, Product, Theme, StoreProfile, generate_store_profile_id

# --- STORE MANAGEMENT VIEWS ---

@login_required
def create_store(request):
    if Store.objects.filter(user=request.user).exists():
        messages.warning(request, "You can only create one store per account.")
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        form = StoreCreationForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.user = request.user      
            try:
                store.save()
                StoreProfile.objects.create(
                    store=store,
                    name=store.name,
                    phone_number=store.store_phone_number,
                    whatsapp_number=store.store_whatsapp_number,
                    profile_id=generate_store_profile_id()
                )
                messages.success(request, f'Store "{store.name}" created successfully!')
                return redirect('stores:theme_page', store_id=store.id)
            except Exception as e:
                messages.error(request, f'Error creating store: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StoreCreationForm()
    
    return render(request, 'stores/create_store.html', {'form': form})

@login_required
def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    products = store.products.all()
    context = {
        'store': store,
        'products': products, 
        'page_title': 'Store Overview' 
    }
    return render(request, 'stores/store_detail.html', context)

@login_required
def select_theme(request, store_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    themes = Theme.objects.filter(is_active=True)
    context = {
        'store': store,
        'themes': themes,
        'page_title': 'Choose a Theme'
    }
    return render(request, 'stores/theme_selection.html', context)

@login_required
def apply_theme(request, store_id):
    if request.method == 'POST':
        store = get_object_or_404(Store, id=store_id, user=request.user)
        theme_id = request.POST.get('theme_id')
        if theme_id:
            try:
                theme = Theme.objects.get(id=theme_id)
                store.active_theme = theme
                store.save()
                messages.success(request, f'Successfully applied the "{theme.name}" theme!')
            except Theme.DoesNotExist:
                messages.error(request, 'The selected theme could not be found.')
        else:
            messages.error(request, 'No theme was selected.')
        return redirect('stores:select_theme', store_id=store.id)
    return redirect('user_dashboard')


@login_required
def theme_page(request, store_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    context = {
        'store': store,
        'page_title': 'Theme Options'
    }
    return render(request, 'stores/theme_page.html', context)

# --- PRODUCT MANAGEMENT VIEWS ---

@login_required
def product_list(request, store_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    products_queryset = store.products.all().order_by('-created_at')
    search_query = request.GET.get('q', '')
    if search_query:
        products_queryset = products_queryset.filter(
            Q(name__icontains=search_query)
        )
    paginator = Paginator(products_queryset, 10)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context = {
        'store': store,
        'products': products,
        'search_query': search_query,
        'page_title': 'Products'
    }
    return render(request, 'stores/product_list.html', context)

@login_required
def add_product(request, store_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store 
            product.save()
            messages.success(request, f'Product "{product.name}" added successfully!')
            return redirect('stores:product_list', store_id=store.id) 
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm()
    context = {
        'form': form,
        'store': store,
        'page_title': 'Add New Product'
    }
    return render(request, 'stores/product_form.html', context)

@login_required
def edit_product(request, store_id, product_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    product = get_object_or_404(Product, id=product_id, store=store) 
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product "{product.name}" updated successfully!')
            return redirect('stores:product_list', store_id=store.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm(instance=product) 
    context = {
        'form': form,
        'store': store,
        'product': product, 
        'page_title': f'Edit Product: {product.name}'
    }
    return render(request, 'stores/product_form.html', context)

@login_required
def delete_product(request, store_id, product_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    product = get_object_or_404(Product, id=product_id, store=store)
    if request.method == 'POST':
        product_name = product.name 
        product.delete()
        messages.success(request, f'Product "{product_name}" has been deleted successfully.')
        return redirect('stores:product_list', store_id=store.id)
    context = {
        'store': store,
        'product': product,
        'page_title': f'Confirm Delete: {product.name}'
    }
    return render(request, 'stores/product_confirm_delete.html', context)