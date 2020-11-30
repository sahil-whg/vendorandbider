from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, UserManager
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Vendor(AbstractBaseUser):
    model = User
    objects = UserManager()
    username = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="email",max_length=90,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    company_name = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=40)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

# Create your models here.
