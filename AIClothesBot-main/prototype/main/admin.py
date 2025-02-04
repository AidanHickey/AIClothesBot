from django.contrib import admin
from .models import Products
from django import forms
from taggit.forms import TagWidget

# Custom form for managing tags
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['productname', 'price', 'category', 'rating', 'tags']
        widgets = {
            'tags': TagWidget()  # Use TagWidget to make tag selection user-friendly
        }

# Register the Product model with the custom form
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('productname', 'price', 'category', 'rating')
    search_fields = ('productname', 'category')
    list_filter = ('category',)

# Register the model and admin class
admin.site.register(Products, ProductAdmin)
