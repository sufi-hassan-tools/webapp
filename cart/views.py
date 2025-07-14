# mystore_project/cart/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from stores.models import Product, Store
from .cart import Cart
from .forms import CartAddProductForm # Import the new form

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = CartAddProductForm(request.POST) # Create an instance of the form with submitted data

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )

    # Get the store from the product
    store = product.store
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    
    # Get the store from the first product in the cart
    store = None
    if len(cart) > 0:
        # Get the first product's ID from the cart
        first_product_id = next(iter(cart.cart.keys()))
        # Get the product and its store
        product = get_object_or_404(Product, id=int(first_product_id))
        store = product.store
    
    return render(request, 'cart/detail.html', {'cart': cart, 'store': store})