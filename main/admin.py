from django.contrib import admin
from .models import Products
from django import forms
from taggit.forms import TagWidget

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['productname', 'price', 'category', 'rating', 'tags']
        widgets = {
            'tags': TagWidget()  
        }

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('productname', 'price', 'category', 'rating', 'type', 'size', 'color') 
    search_fields = ('productname', 'category')
    list_filter = ('category', 'type', 'size', 'color')  
    fields = ('productname', 'price', 'category', 'rating', 'tags', 'type', 'size', 'color')  

admin.site.register(Products, ProductAdmin)
