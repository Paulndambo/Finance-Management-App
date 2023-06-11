from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from lipia.models import MpesaTransaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                validated_data["username"], validated_data["email"], validated_data["password"])
            
            profile = Profile.objects.create(
                user=user
            )
            return user
        except Exception as e:
            raise e


class ProfileSerializer(serializers.ModelSerializer):
    mpesa_transactions_total = serializers.SerializerMethodField()
    mpesa_transactions = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = '__all__'
    
    def get_mpesa_transactions(self, instance):
        transactions = MpesaTransaction.objects.filter(phone_number=instance.phone_number)
        if transactions:
            return transactions.values()
        else:
            return []
        
    def get_mpesa_transactions_total(self, instance):
        transactions = MpesaTransaction.objects.filter(phone_number=instance.phone_number)
        if transactions:
            return sum(transactions.values_list('amount', flat=True))
        else:
            return 0