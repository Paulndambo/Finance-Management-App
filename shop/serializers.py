from rest_framework import serializers
from .models import Shop, ShopStock

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"



class ShopStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopStock
        fields = "__all__"