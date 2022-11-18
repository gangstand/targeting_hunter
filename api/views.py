from django.shortcuts import render
from rest_framework import generics

from api.models import Category, Preferencies, SaleCart
from api.serializer import CategorySerializer, PreferenciesSerializer, SaleCartSerializer


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PreferenciesAPIList(generics.ListCreateAPIView):
    queryset = Preferencies.objects.all()
    serializer_class = PreferenciesSerializer


class PreferenciesAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Preferencies.objects.all()
    serializer_class = PreferenciesSerializer

class SaleCartAPIList(generics.ListCreateAPIView):
    queryset = SaleCart.objects.all()
    serializer_class = SaleCartSerializer


class SaleCartAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleCart.objects.all()
    serializer_class = SaleCartSerializer