from django.contrib import admin

from api.models import Category, Preferencies, SaleCart, Product

admin.site.register(Product)
admin.site.register(Preferencies)
admin.site.register(Category)
admin.site.register(SaleCart)
