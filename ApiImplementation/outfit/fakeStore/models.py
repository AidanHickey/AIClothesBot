from django.db import models

class Product(models.Model):
    
    title=models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    category = models.CharField(max_length=100)
    description = models.TextField()  
    image = models.URLField()
    def __str__(self):
        return self.title