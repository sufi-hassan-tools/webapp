# This is the full code for mystore_project/accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, CustomLoginForm
from stores.models import Store 

# Custom login view that uses a form with 'email' instead of 'username'
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomLoginForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('user_dashboard')

@login_required
def user_dashboard(request):
    # This view is already protected by @login_required
    user_stores = Store.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'stores': user_stores
    }
    return render(request, 'accounts/user_dashboard.html', context)

def register(request):
    # Redirect already authenticated users
    if request.user.is_authenticated:
        return redirect('user_dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})