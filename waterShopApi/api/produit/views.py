from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProduitSerializer
from .models import Produits

# Create your views here.

class ProduitsViewSet(viewsets.ModelViewSet):
    queryset = Produits.objects.all().order_by('nom')
    serializer_class = ProduitSerializer
