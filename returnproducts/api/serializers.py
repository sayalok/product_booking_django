from rest_framework import serializers

from returnproducts.models import ReturnProducts

class ReturnProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ReturnProducts
        fields  = '__all__'
