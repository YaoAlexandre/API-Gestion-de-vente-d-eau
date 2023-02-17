from .models import Categories
from rest_framework import serializers

class CategorieSerializer(serializers.ModelSerializer):
    produits = serializers.StringRelatedField(many=True)
    class Meta:
        model = Categories
        fields = {"nom", "description", "produits"}
        fields = '__all__'