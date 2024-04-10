from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    text = serializers.CharField()

    class Meta:
        model = Product
        fields = ['text',]
