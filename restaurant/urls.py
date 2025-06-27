from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import FoodViewSet, TagViewSet

router=DefaultRouter() #setting router
router.register(r'foods', FoodViewSet)
router.register(r'tags',TagViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
