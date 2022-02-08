from rest_framework import generics
from returnproducts.models import ReturnProducts
from .serializers import ReturnProductsSerializer
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.db import transaction
from products.models import Product
from datetime import datetime


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
            with transaction.atomic():
                new_return_product = ReturnProducts.objects.create(
                    from_date = return_product_data["from_date"], 
                    to_date = return_product_data["to_date"], 
                    total = return_product_data['total'],
                    product_id = return_product_data['product_id'],
                    milage = return_product_data['milage']
                )
                new_return_product.save()
                productById = Product.objects.get(pk=return_product_data['product_id'])
                if return_product_data['milage'] != 0:
                    dateDiff = datetime.strptime(str(return_product_data["to_date"]), "%Y-%m-%d") - datetime.strptime(str(return_product_data["from_date"]), "%Y-%m-%d")

                    if productById.type == 'plain':
                        newdur = productById.durability - ((dateDiff.days+1) * 1)
                    else:
                        milagePOint = (int(return_product_data['milage']) / 10) * 2
                        datePoint = productById.durability - ((dateDiff.days+1) * 2) 
                        newdur = productById.durability - (milagePOint - datePoint)
                    
                Product.objects.filter(pk=return_product_data['product_id']).update(availability=0, durability=newdur)
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