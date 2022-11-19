from rest_framework import serializers

from accounts.models import CustomUser
from api.models import Category, Preferencies, SaleCart, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PreferenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferencies
        fields = '__all__'


class SaleCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleCart
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
