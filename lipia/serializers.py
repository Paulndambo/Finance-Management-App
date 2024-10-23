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


class C2BConfirmationSerializer(serializers.Serializer):
   TransactionType = serializers.CharField(max_length=255, required=False)
   TransID = serializers.CharField(max_length=255, required=False)
   TransTime = serializers.CharField(max_length=255, required=False)
   TransAmount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
   BusinessShortCode = serializers.CharField(max_length=255, required=False)
   BillRefNumber = serializers.CharField(max_length=255, required=False)
   InvoiceNumber = serializers.CharField(max_length=255, required=False)
   OrgAccountBalance = serializers.CharField(max_length=255, required=False)
   ThirdPartyTransID = serializers.CharField(max_length=255, required=False)
   MSISDN = serializers.CharField(max_length=255, required=False)
   FirstName = serializers.CharField(max_length=255, required=False)
   MiddleName = serializers.CharField(max_length=255, required=False)
   LastName = serializers.CharField(max_length=255, required=False)