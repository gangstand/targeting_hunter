import json
from base64 import encode

from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import generics

from accounts.models import CustomUser
from api.models import Category, Preferencies, SaleCart, Product
from api.serializer import CategorySerializer, PreferenciesSerializer, SaleCartSerializer, UserSerializer, \
    ProductSerializer


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


class UserAPIList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def getUserPreferencies(request):
    user_id = request.GET.get('user_id')
    prefer = Preferencies.objects.filter(user_id=user_id)
    cat = json.loads(serializers.serialize('json', [pr.category_id for pr in prefer]))
    pr = json.loads(serializers.serialize('json', [pr for pr in prefer]))
    res = []
    for i in range(len(cat)):
        res.append({
            'prefer': pr[i]['fields'],
            'category': cat[i]['fields']
        })


    with open('try_unicode.json', 'w') as f:
        res = json.dumps(res, indent=2, ensure_ascii=False)

    print(res, type(res))

    return HttpResponse(res, content_type='application/json')

def getCategoryProducts(request):
    category = Product.objects.all()
    products = json.loads(serializers.serialize('json', category))
    res = [product['fields'] for product in products]

    return HttpResponse(category, content_type='application/json')
