from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
import json
from django.http import JsonResponse
import requests
from django.core.paginator import Paginator


def index(request):
    return render(request, 'dashboard.html')

def marketplace(request):
    response = requests.get("https://fakestoreapi.com/products/category/men's clothing")
    data = response.json()
    for p in data:
        if not Products.objects.filter(productname=p['title'],price=p['price'],image=p['image'],category=p['category']):
            b = Products(productname=p['title'],price=p['price'],image=p['image'],category=p['category'])
            b.save()

    response = requests.get("https://fakestoreapi.com/products/category/women's clothing")
    data = response.json()
    for p in data:
        if not Products.objects.filter(productname=p['title'],price=p['price'],image=p['image'],category=p['category']):
            b = Products(productname=p['title'],price=p['price'],image=p['image'],category=p['category'])
            b.save()


    product_list = Products.objects.all()
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    return render(request, 'marketplace.html', {'products':products})