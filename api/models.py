import uuid

from django.db import models

from accounts.models import BasePeopleColor, UserBaseData, CustomUser


class Category(BasePeopleColor, UserBaseData):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Название категории', max_length=255)


class Preferencies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, verbose_name='ID пользователя', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', verbose_name='ID категории', on_delete=models.CASCADE)
    degree = models.IntegerField(verbose_name='Степень важности', )


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    cost = models.IntegerField(verbose_name='Цена')
    category_id = models.ForeignKey('Category', verbose_name='ID категории', on_delete=models.CASCADE)
    indevirator = models.IntegerField(verbose_name="Индификатор")
    cloth = models.CharField(verbose_name='Цвет товара (одежды)', max_length=255, blank=True, null=True)


class SaleCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, verbose_name='ID пользователя', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Счет')

