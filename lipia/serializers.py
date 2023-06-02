from .models import MpesaResponseBody, ServiceProvider, MpesaTransaction
from rest_framework import serializers
from core.constants import PAYMENT_NUMBER_TYPES

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


class CustomerToBusinessLipaNaMpesaSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=255)
    amount = serializers.DecimalField(max_digits=50, decimal_places=2)
    pay_type = serializers.CharField(max_length=255)
    business_number = serializers.CharField(max_length=255)