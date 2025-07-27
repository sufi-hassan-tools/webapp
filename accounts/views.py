# This is the full code for mystore_project/accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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
    """Display the dashboard for the logged in user.

    If the user has created a store (their StoreProfile), display the store
    details.  Otherwise show a call to action to create one.
    """

    store_profile = Store.objects.filter(user=request.user).first()
    if not store_profile:
        messages.info(request, "You don't have a store yet. Create one to get started!")

    context = {
        'store_profile': store_profile,
    }
    return render(request, 'accounts/user_dashboard.html', context)

from .models import UserProfile

def register(request):
    # Redirect already authenticated users
    if request.user.is_authenticated:
        return redirect('user_dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            
            # Create UserProfile
            UserProfile.objects.create(
                user=user,
                name=form.cleaned_data.get('name'),
                phone_number=form.cleaned_data.get('phone_number'),
                profile_picture=form.cleaned_data.get('profile_picture')
            )

            login(request, user)  # Log the user in
            messages.success(request, "Account created successfully!")
            return redirect('user_dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
