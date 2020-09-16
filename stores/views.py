# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializes, StoreSerializes, ProductDetailSerializes
from .models import Product, Store
from rest_framework.response import Response
# from rest_framework.permissions import Rea

# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializes
    queryset = Product.objects.all()
    # permission_classes=[ReadOnl]

    def get_serializer_class(self):
        if self.action=='list':
            print(self.action)
        # return Response(self.queryset)

        


    


class Storeviewset(viewsets.ModelViewSet):
    serializer_class = StoreSerializes
    queryset = Store.objects.all()
