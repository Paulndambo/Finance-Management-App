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