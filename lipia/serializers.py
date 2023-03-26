from .models import MpesaResponseBody, ServiceProvider, MpesaTransaction
from rest_framework import serializers

class MpesaResponseBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaResponseBody
        fields = "__all__"



class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = "__all__"


class MpesaTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaTransaction
        fields = "__all__"


class LipaNaMpesaSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)