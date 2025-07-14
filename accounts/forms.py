from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model() # Gets our custom User model

class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Full Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Your Email Address'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'email') # 'password1' and 'password2' are handled by UserCreationForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure email field is correctly configured if using it as username
        if 'username' in self.fields: # Default UserCreationForm might use 'username'
            del self.fields['username'] # We don't need a separate username field

class CustomLoginForm(AuthenticationForm):
    """
    Custom login form that replaces 'username' field label with 'email'
    and adds appropriate styling/placeholders
    """
    username = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email Address',
            'id': 'id_email'
        })
    )
    
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Password',
            'id': 'id_password'
        })
    )