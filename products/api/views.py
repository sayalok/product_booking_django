from rest_framework.generics import (
    ListAPIView, 
)
from products.models import Product
from .serializers import (
    ProductsListSerializer
)

from rest_framework.response import Response

class ProductListView(ListAPIView):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductsListSerializer(queryset, many=True)
        return Response({"status":'Success',"data":serializer.data})