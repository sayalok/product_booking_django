from rest_framework import generics
from returnproducts.models import ReturnProducts
from .serializers import ReturnProductsSerializer

from rest_framework.response import Response

class ReturnProductsListView(generics.ListCreateAPIView):
    queryset = ReturnProducts.objects.all()
    serializer_class = ReturnProductsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ReturnProductsSerializer(queryset, many=True)
        return Response({"status":'Success',"data":serializer.data})

    def perform_create(self, serializers):
        serializers.save()

    # overriding the method for sending custom message
    def post(self, request, *args, **kwargs):
        self.create(request,*args, **kwargs)
        return Response({"status":'Success'})