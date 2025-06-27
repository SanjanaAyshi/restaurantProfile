from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
# Create your views here.

class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')   # fixed
    serializer_class = ContactSerializer
