from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.


class GerantsViewSet(viewsets.ModelViewSet):
    queryset = Gerant.objects.all().order_by('last_name')
    serializer_class = GerantSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('last_name')
    serializer_class = ClientSerializer


class LivreursViewSet(viewsets.ModelViewSet):
    queryset = Livreur.objects.all().order_by('last_name')
    serializer_class = LivreurSerializer
