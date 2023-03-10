from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    last_name = models.CharField(max_length= 100)
    first_name = models.CharField(max_length= 50)
    email = models.CharField(max_length= 255, unique= True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

