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

