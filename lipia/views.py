from django.shortcuts import render
from .serializers import MpesaResponseBodySerializer
from .models import MpesaResponseBody

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class MpesaViewSet(ModelViewSet):
    queryset = MpesaResponseBody.objects.all()
    serializer_class = MpesaResponseBodySerializer

    def create(self, request, *args, **kwargs):
        body = request.data["Body"]
        print("***************Callback Data***************")
        print(body)
        print("***************Callback Data***************")

        if body:
            mpesa = MpesaResponseBody.objects.create(body=body)
            return Response({"message": "Transaction Successful!!"}, status=status.HTTP_201_CREATED)
        return Response({"failed": "Transaction Failed"}, status=status.HTTP_400_BAD_REQUEST)


body = {'stkCallback': {'MerchantRequestID': '101035-71435381-1', 'CheckoutRequestID': 'ws_CO_11032023030458446745491093', 'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 'CallbackMetadata': {
    'Item': [{'Name': 'Amount', 'Value': 1.0}, {'Name': 'MpesaReceiptNumber', 'Value': 'RCB2IF7UX4'}, {'Name': 'Balance'}, {'Name': 'TransactionDate', 'Value': 20230311030509}, {'Name': 'PhoneNumber', 'Value': 254745491093}]}}}
