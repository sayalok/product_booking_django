from rest_framework import serializers

from returnproducts.models import ReturnProducts

class ReturnProductsSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model   = ReturnProducts
        fields  = '__all__'
