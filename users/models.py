from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, user_type=None, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The First Name field must be set')
        if not last_name:
            raise ValueError('The Last Name field must be set')


        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user_type=user_type
        user.is_staff = is_staff
        user.is_active = True
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password=None, user_type='admin'):
        user = self.create_user(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            password=password,
            user_type=user_type,
            is_staff=True,
            is_superuser=True
            )
        user.save()
 
        return user

class User(auth_models.AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20, default='applicant')
    company_id = models.IntegerField(null=True)
    username = None
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

