from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

MALE = [
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский'),
]


class BasePeopleColor(models.Model):
    header = models.CharField(verbose_name='Цвета одежды на голове', max_length=256)
    torso = models.CharField(verbose_name='Цвета одежды на торсе', max_length=256)
    legs = models.CharField(verbose_name='Цвета одежды ног', max_length=256)

    class Meta:
        abstract = True


class BioDataBaseModel(models.Model):
    face = models.FileField(verbose_name='Лицо II', max_length=256, null=False)

    class Meta:
        abstract = True


class UserBaseData(models.Model):
    patronymic = models.CharField(verbose_name='Отчество', max_length=256)
    age = models.IntegerField(verbose_name='Возраст', blank=True, null=True)
    male = models.CharField(choices=MALE, verbose_name='Пол', max_length=256)
    nationality = models.CharField(verbose_name='Национальность', max_length=256)
    kid = models.BooleanField(verbose_name='Ребенок', blank=True, null=True, default=None)
    animal = models.BooleanField(verbose_name='Животное', blank=True, null=True, default=None)
    is_moderator = models.BooleanField(verbose_name='Модерирование',  blank=True, null=False, default=False)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, BasePeopleColor, BioDataBaseModel, UserBaseData):
    moderator = models.BooleanField(verbose_name='Модератор', blank=True, null=True, default=False)

    def __str__(self):
        return f"{self.last_name}" + f"{self.first_name}"
