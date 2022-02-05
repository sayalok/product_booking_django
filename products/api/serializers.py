from rest_framework import serializers

from products.models import Product

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Product
        fields  = '__all__'
