from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, title, phone, location, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, title=title, phone=phone, location=location)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, title, phone, location, password=None):
        user = self.create_user(email, title, phone, location, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    users_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True, null=False)
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    password = models.CharField(max_length=128, default="")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["title", "phone", "location"]

    def __str__(self):
        return self.email
