from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'gerant', GerantsViewSet)
router.register(r'livreur', LivreurSerializer)
router.register(r'client', ClientSerializer)

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(routerLivreur.urls)),
    # path('', include(routerClient.urls)),
]