import uuid

from django.db import models

from accounts.models import BasePeopleColor, UserBaseData, CustomUser

MALE = [
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский'),
]

class Category(BasePeopleColor):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Название категории', max_length=255)
    age = models.IntegerField(verbose_name='Возраст', blank=True, null=True)
    male = models.CharField(choices=MALE, verbose_name='Пол', max_length=256, blank=True, null=True)
    kid = models.BooleanField(verbose_name='Ребенок', blank=True, null=True, default=None)
    animal = models.BooleanField(verbose_name='Животное', blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.name}"


class Preferencies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, verbose_name='ID пользователя', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, verbose_name='ID категории', on_delete=models.CASCADE)
    degree = models.IntegerField(verbose_name='Степень важности', )


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    cost = models.IntegerField(verbose_name='Цена')
    category_id = models.ForeignKey('Category', verbose_name='ID категории', on_delete=models.CASCADE)
    indevirator = models.IntegerField(verbose_name="Индификатор")
    cloth = models.CharField(verbose_name='Цвет товара (одежды)', max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}_{self.category_id}"

class SaleCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(CustomUser, verbose_name='ID пользователя', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Счет')

