from django.shortcuts import render
from .serializers import (
    MpesaResponseBodySerializer,
    ServiceProviderSerializer, 
    MpesaTransactionSerializer,
    LipaNaMpesaSerializer,
    CustomerToBusinessLipaNaMpesaSerializer
)
from .models import MpesaResponseBody, ServiceProvider, MpesaTransaction
from .mpesa_metadata_transformer import mpesa_metadata_transformative_function
from .utils import MpesaGateWay



from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, generics


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


class LipaNaMpesaGenericAPIView(generics.CreateAPIView):
    serializer_class = LipaNaMpesaSerializer

    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            cl = MpesaGateWay()
            cl.stk_push(
                phone_number=data.get('phone_number'),
                amount=int(data.get('amount')),
                callback_url="https://f735-105-160-117-204.ngrok-free.app/lipia/lipa-na-mpesa/",
                account_reference="Perfin Mpesa",
                transaction_desc="This is perfin mpesa transaction"
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"failed": "Payment Request Failed!!"}, status=status.HTTP_400_BAD_REQUEST)



class C2BLipaNaMpesaGenericAPIView(generics.CreateAPIView):
    serializer_class = CustomerToBusinessLipaNaMpesaSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)