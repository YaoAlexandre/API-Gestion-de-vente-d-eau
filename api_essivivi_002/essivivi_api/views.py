from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

# View For Categories
class ListCategories(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorieSerializer

class DetailCategories(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorieSerializer

# View For Eau
class ListEau(generics.ListCreateAPIView):
    queryset = Eau.objects.all()
    serializer_class = EauSerializer

class DetailEau(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eau.objects.all()
    serializer_class = EauSerializer

# View For Produit
class ListProduit(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class DetailProduit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
