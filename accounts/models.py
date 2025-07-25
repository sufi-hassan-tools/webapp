# This is the full and correct code for mystore_project/accounts/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.conf import settings
import string
import random

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) # Users are active by default
    date_joined = models.DateTimeField(default=timezone.now)

    # Link the custom manager
    objects = CustomUserManager()

    # Set the email field as the unique identifier
    USERNAME_FIELD = 'email'
    # Required fields when creating a user via createsuperuser
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    # Add related_name to avoid clashes if you ever had the default User model migrated
    # For a fresh setup where default User was never migrated, these might not strictly be needed
    # but it's good practice if there's any doubt.
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_account_set", # Ensure this is unique
        related_query_name="user_account",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_account_set", # Ensure this is unique
        related_query_name="user_account",
    )

def generate_profile_id():
    """Generate a unique 8-character alphanumeric ID."""
    length = 8
    characters = string.ascii_letters + string.digits
    while True:
        profile_id = ''.join(random.choice(characters) for i in range(length))
        if not UserProfile.objects.filter(profile_id=profile_id).exists():
            return profile_id

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    profile_id = models.CharField(max_length=8, unique=True, default=generate_profile_id)
    name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.email
