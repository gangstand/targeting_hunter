from django.urls import path

from .views import *

urlpatterns = [
    path('category', CategoryAPIList.as_view()),
    path('category/<int:pk>/', CategoryAPIUpdateDestroy.as_view()),
    path('preferencies', PreferenciesAPIList.as_view()),
    path('preferencies/<int:pk>/', PreferenciesAPIUpdateDestroy.as_view()),
    path('salecart', SaleCartAPIList.as_view()),
    path('salecart/<int:pk>/', SaleCartAPIList.as_view()),
    path('product', ProductAPIList.as_view()),
    path('product/<int:pk>/', ProductAPIUpdateDestroy.as_view()),
    path('user', UserAPIList.as_view()),
    path('prefer', getUserPreferencies),
    path('products', getCategoryProducts)

]
