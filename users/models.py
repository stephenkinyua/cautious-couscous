from enum import unique
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .model_managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
        Custom user model that supports using email instead of username
    """
    email = None
    phone_number = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Assign user manager to the object's attributes
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
