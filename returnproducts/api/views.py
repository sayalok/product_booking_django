from rest_framework import generics
from returnproducts.models import ReturnProducts
from .serializers import ReturnProductsSerializer
from django.db import IntegrityError
from django.core.exceptions import ValidationError


from rest_framework.response import Response

class ReturnProductsListView(generics.ListCreateAPIView):
    queryset = ReturnProducts.objects.all()
    serializer_class = ReturnProductsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ReturnProductsSerializer(queryset, many=True)
        return Response({"status":'Success',"data":serializer.data})

    def create(self, request, *args, **kwargs):
        return_product_data = request.data
        try:
            new_return_product = ReturnProducts.objects.create(
                from_date = return_product_data["from_date"], 
                to_date = return_product_data["to_date"], 
                total = return_product_data['total'],
                product_id = return_product_data['product_id'],
                milage = return_product_data['milage']
            )
            new_return_product.save()
            return {'status': True}
        except IntegrityError:
            return {
                'status': False,
                'message': 'Can not save data'
            }
        except ValidationError as e:
            return {
                'status': False,
                'message': 'Not valid data'
            }

    # overriding the method for sending custom message
    def post(self, request, *args, **kwargs):
        result = self.create(request,*args, **kwargs)
        if result['status']:
            return Response({"status":'Success'})
        else:
            return Response({
                "status":'Failed',
                'message': result['message']
            })