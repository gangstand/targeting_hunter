from django.contrib import admin

from api.models import Category, Preferencies, SaleCart

admin.site.register(Preferencies)
admin.site.register(Category)
admin.site.register(SaleCart)
