from rest_framework import generics
from booking.models import Booking
from .serializers import BookingSerializer

from rest_framework.response import Response

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookingSerializer(queryset, many=True)
        return Response({"status":'Success',"data":serializer.data})

    def perform_create(self, serializers):
        serializers.save()

    # overriding the method for sending custom message
    def post(self, request, *args, **kwargs):
        self.create(request,*args, **kwargs)
        return Response({"status":'Success'})