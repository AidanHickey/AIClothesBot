import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(["GET"])
def fetch_products(request):
    # Fetch from the external API
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        products_data = response.json()

        
        Product.objects.all().delete()

        
        for product_data in products_data:
            serializer = ProductSerializer(data=product_data)
            if serializer.is_valid():
                serializer.save()

        # Now fetch from the database
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data)

    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=500)