from rest_framework import serializers


class PaymentRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    phone_number = serializers.CharField(max_length=255)
    payer_email = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)