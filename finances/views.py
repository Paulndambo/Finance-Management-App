from django.shortcuts import render
from django.db import transaction

from rest_framework import generics, status
from rest_framework.response import Response

from finances.models import Expenditure
from finances.serializers import ExpenditureSerializer
# Create your views here.
class ExpenditureAPIView(generics.ListCreateAPIView):
    queryset = Expenditure.objects.all().order_by("-created")
    serializer_class = ExpenditureSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
