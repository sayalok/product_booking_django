from rest_framework import generics
from booking.models import Booking
from products.models import Product
from .serializers import BookingSerializer
from django.db import IntegrityError
from django.core.exceptions import ValidationError


from rest_framework.response import Response

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookingSerializer(queryset, many=True)
        return Response({"status":'Success',"data":serializer.data})

    def create(self, request, *args, **kwargs):
        booking_data = request.data
        try:
            new_booking = Booking.objects.create(
                from_date = booking_data["from_date"], 
                to_date = booking_data["to_date"], 
                total = booking_data['total'],
                product_id = booking_data['product_id']
            )
            new_booking.save()
            return {'status': True}
        except IntegrityError as e:
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