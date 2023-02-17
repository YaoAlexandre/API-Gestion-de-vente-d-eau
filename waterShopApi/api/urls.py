from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.getRoute),
    path('categories/', include('api.categorie.urls')),
    path('produits/', include('api.produit.urls')),
    # path('gerant/', include('api.users.urls')),
    # path('livreur/', include('api.users.urls')),
    # path('client/', include('api.users.urls')),
    path('login/', include('api.authentication.urls'))
]