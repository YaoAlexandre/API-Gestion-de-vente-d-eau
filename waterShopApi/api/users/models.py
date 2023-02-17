from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    adresse = models.CharField(max_length= 255)
    telephone = models.CharField(max_length= 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gerant(User):
       nom_ste = models.CharField(max_length= 255)


class Livreur(User):
    code_livreur = models.CharField(max_length=6)
    gerants = models.ForeignKey(
        Gerant,
        on_delete= models.SET_NULL,
        related_name= "livreurs",
        blank= True,
        null= True
    )

class Client(User):
    code_client = models.CharField(max_length = 6)
    livreurs = models.ForeignKey(
        Livreur,
        on_delete= models.SET_NULL,
        related_name= "clients",
        blank= True,
        null= True
    )