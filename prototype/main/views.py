from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


def index(request):
    return render(request, 'dashboard.html')

def marketplace(request):
    products = Products.objects.all()

    return render(request, 'marketplace.html', {'products':products})