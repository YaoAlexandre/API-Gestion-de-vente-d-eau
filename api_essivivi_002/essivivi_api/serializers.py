from rest_framework import serializers
from .models import *

class CategorieSerializer(serializers.ModelSerializer):
    #produits = serializers.StringRelatedField(many=True)
    class Meta:
        model = Categories
        fields = {"id", "title", "description", "produits"}
        fields = '__all__'


class EauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eau
        fields = {
            "id", 
            "categorie",
            "title", 
            "description", 
            "prix", 
            "volume", 
            "stock", 
            "imagUrl", 
            "statut",
            "created_at"
        }
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = {
            "id", 
            "categorie",
            "produit_tag",
            "nom", 
            "description", 
            "prix", 
            "stock", 
            "imagUrl", 
            "statut",
            "created_at"
        }
        fields = '__all__'