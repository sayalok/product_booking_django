from rest_framework import serializers

from returnproducts.models import ReturnProducts
from products.api.serializers import ProductsSerializer


class ReturnProductsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(read_only=True)

    class Meta:
        model   = ReturnProducts
        fields  = '__all__'
