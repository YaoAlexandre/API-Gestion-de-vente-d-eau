from django.urls import path
from .views import *



urlpatterns = [
   path('categories', ListCategories.as_view(), name= 'categories'),
   path('categories/<int:pk>/', DetailCategories.as_view(), name= 'categoriesById'),

   path('produits', ListProduit.as_view(), name= 'produits'),
   path('produits/<int:pk>/', DetailProduit.as_view(), name= 'produitsById'),

   path('eaux', ListEau.as_view(), name= 'eaux'),
   path('eaux/<int:pk>/', DetailEau.as_view(), name= 'eauxById'),
]