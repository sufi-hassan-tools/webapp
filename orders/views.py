# mystore_project/orders/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib import messages

def order_create(request):
    cart = Cart(request)
    
    # Check if cart is empty
    if not cart:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:cart_detail')
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            
            # Validate that all items in cart are from the same store
            cart_items = list(cart)
            if not cart_items:
                messages.error(request, 'Your cart is empty.')
                return redirect('cart:cart_detail')
            
            # Get the store from the first item
            first_product = cart_items[0]['product']
            store = first_product.store
            
            # Check if all items are from the same store
            for item in cart_items:
                if item['product'].store != store:
                    messages.error(request, 'All items in your cart must be from the same store.')
                    return redirect('cart:cart_detail')
            
            # Check stock availability
            for item in cart_items:
                product = item['product']
                quantity = item['quantity']
                if product.stock_quantity < quantity:
                    messages.error(request, f'Insufficient stock for {product.name}. Available: {product.stock_quantity}')
                    return redirect('cart:cart_detail')
            
            # Associate order with store
            order.store = store
            
            # If user is authenticated, you could associate the order with the user here
            # if request.user.is_authenticated:
            #     order.user = request.user
            
            order.save()

            # Create order items and update stock
            for item in cart_items:
                product = item['product']
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item['price'],
                    quantity=item['quantity']
                )
                
                # Update stock quantity
                product.stock_quantity -= item['quantity']
                if product.stock_quantity == 0:
                    product.is_available = False
                product.save()
            
            # Clear the cart
            cart.clear()
            messages.success(request, 'Your order has been successfully placed!')
            return redirect('storefront:store_home', store_id=order.store.id)
    else:
        form = OrderCreateForm()

    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})