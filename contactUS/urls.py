from rest_framework.routers import DefaultRouter
from .views import ContactViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r'contacts', ContactViewset)

urlpatterns = [
    path('', include(router.urls)),
]
