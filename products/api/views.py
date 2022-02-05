from rest_framework import generics
from products.models import Product
from .serializers import ProductsSerializer

from rest_framework.response import Response

class ProductListView(generics.ListAPIView):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response({"status":'Success',"data":serializer.data})