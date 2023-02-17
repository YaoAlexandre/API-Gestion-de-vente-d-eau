from django.db import models
from api.categorie.models import Categories
from api.users.models import Gerant
from api.users.models import *
from django.db import models

# Create your models here.

class Produits(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    prix = models.IntegerField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to= 'images/', blank=True, null=True)
    categories_id = models.ForeignKey(
        Categories, 
        on_delete= models.SET_NULL, 
        related_name='produits',
        blank=True, 
        null= True)
    gerant = models.ForeignKey(
        Gerant,
        on_delete= models.SET_NULL,
        related_name= "gerant",
        blank= True,
        null= True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True) 

    def __str__(self):
        return self.nom
