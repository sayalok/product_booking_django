from rest_framework import serializers

from booking.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model   = Booking
        fields  = '__all__'
