from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from .serializers import ShopSerializer, ShopStockSerializer
from .models import Shop, ShopStock
# Create your views here.
class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopStockModelViewSet(ModelViewSet):
    queryset = ShopStock.objects.all()
    serializer_class = ShopStockSerializer
