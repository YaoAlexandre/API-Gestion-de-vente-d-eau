from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorieSerializer
from .models import Categories

# Create your views here.

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('nom')
    serializer_class = CategorieSerializer