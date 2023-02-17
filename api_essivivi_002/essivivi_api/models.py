from django.db import models

# Create your models here.

class Categories(models.Model):
    title = models.CharField( max_length= 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Catégoires'

    def __str__(self):
        return self.title

class Eau(models.Model):
    title = models.CharField(max_length=100)
    categorie = models.ForeignKey(
        Categories, 
        on_delete= models.CASCADE, 
        related_name='eaux',
        blank=True, 
        null= True)
    description = models.TextField()
    volume = models.IntegerField()
    prix = models.IntegerField()
    stock = models.IntegerField()
    statut = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to= 'images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True) 

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Eaux'

    def __str__(self):
        return self.title


class Produit(models.Model):
    produit_tag = models.CharField(max_length= 10)
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(
        Categories, 
        on_delete= models.CASCADE, 
        related_name='produits',
        blank=True, 
        null= True)
    description = models.TextField()
    prix = models.IntegerField()
    stock = models.IntegerField()
    statut = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to= 'images/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} {}'.format(self.produit_tag, self.nom) 