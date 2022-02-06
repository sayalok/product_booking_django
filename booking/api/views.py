from rest_framework import generics
from booking.models import Booking
from products.models import Product
from .serializers import BookingSerializer

from rest_framework.response import Response

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookingSerializer(queryset, many=True)
        return Response({"status":'Success',"data":serializer.data})

    # def perform_create(self, serializers):
    #     serializers.save()

    def create(self, request, *args, **kwargs):
        booking_data = request.data
        new_booking = Booking.objects.create(
            from_date = booking_data["from_date"], 
            to_date = booking_data["to_date"], 
            total = booking_data['total'],
            product_id = booking_data['product_id']
        )
        new_booking.save()

    # overriding the method for sending custom message
    def post(self, request, *args, **kwargs):
        self.create(request,*args, **kwargs)
        return Response({"status":'Success'})