from .models import Produits
from rest_framework import serializers

class ProduitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produits
        fields = {"nom", "description", "prix", "stock", "categories_id"}
        fields = '__all__'