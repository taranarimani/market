from rest_framework import serializers
from .models import Product, Store


class ProductSerializes(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name','price']
        read_only_fields = ['id']


class StoreSerializes(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ['id']




class ProductDetailSerializes(ProductSerializes):

    class Meta:
        model = Product
        fields = '__all__'
        
