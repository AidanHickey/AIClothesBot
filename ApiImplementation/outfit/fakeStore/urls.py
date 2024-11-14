from django.urls import  path
from .views import fetch_products

urlpatterns = [
    path('products/', fetch_products)
]
