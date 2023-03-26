from django.shortcuts import render
from .serializers import (
    MpesaResponseBodySerializer,
    ServiceProviderSerializer, 
    MpesaTransactionSerializer
)
from .models import MpesaResponseBody, ServiceProvider, MpesaTransaction

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, generics
from .mpesa_metadata_transformer import mpesa_metadata_transformative_function
# Create your views here.
class MpesaViewSet(ModelViewSet):
    queryset = MpesaResponseBody.objects.all()
    serializer_class = MpesaResponseBodySerializer

    def create(self, request, *args, **kwargs):
        body = request.data["Body"]
        
        if body:
            mpesa = MpesaResponseBody.objects.create(body=body)
            transformed_mpesa_response = mpesa_metadata_transformative_function(body['stkCallback'])
            serializer = MpesaTransactionSerializer(data=transformed_mpesa_response)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"failed": "Transaction Failed"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"failed": "The Transaction has not send callback data"}, status=status.HTTP_400_BAD_REQUEST)


class ServiceProviderViewSet(ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer


class MpesaTransactionViewSet(ModelViewSet):
    queryset = MpesaTransaction.objects.all()
    serializer_class = MpesaTransactionSerializer



