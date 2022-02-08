from rest_framework import serializers

from booking.models import Booking
from products.api.serializers import ProductsSerializer

class BookingSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(read_only=True)

    class Meta:
        model   = Booking
        fields  = '__all__'
