# This is the full code for mystore_project/accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views as account_custom_views

urlpatterns = [
    path('register/', account_custom_views.register, name='register'),
    path('login/', account_custom_views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Using the secure POST method setup
    path('dashboard/', account_custom_views.user_dashboard, name='user_dashboard'),

    # --- NEW: Password Reset URLs ---
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), 
         name='password_reset'),

    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), 
         name='password_reset_confirm'),

    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), 
         name='password_reset_complete'),
]