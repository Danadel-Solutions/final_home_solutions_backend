from api.permissions import IsAuthorOrReadOnly
from api.serializers import PropertySerializer
from .models import Property
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.
# class PropertyListView(generics.ListCreateAPIView):
#     queryset = Property.objects.all()
#     serializer_class = PropertySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
# class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Property.objects.all()
#     serializer_class = PropertySerializer
#     permission_classes = (IsAuthorOrReadOnly,)
class PropertyViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Property.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PropertySerializer