from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
