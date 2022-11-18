from rest_framework import serializers

from api.models import Category, Preferencies, SaleCart


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
