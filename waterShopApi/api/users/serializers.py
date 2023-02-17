from .models import *
from rest_framework import serializers

class GerantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gerant
        fields= ['username', 'first_name', 'last_name', 'nom_ste', 'email', 'password', 'adresse', 'telephone', 'livreurs'] 
        fields = '__all__'

class LivreurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livreur
        fields= ['code_livreur', 'username', 'first_name', 'last_name', 'email', 'password', 'adresse', 'telephone', 'clients'] 
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields= ['code_client' 'first_name', 'last_name', 'email', 'adresse', 'telephone'] 
        fields = '__all__'