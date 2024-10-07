from django.shortcuts import render
from django.db import transaction

from rest_framework import generics, status
from rest_framework.response import Response

from budgets.models import Budget, BudgetAllocation
from budgets.serializers import BudgetAllocationSerializer
# Create your views here.
class BudgetAllocationListCreateView(generics.ListCreateAPIView):
    queryset = BudgetAllocation.objects.all().order_by("-created")
    serializer_class = BudgetAllocationSerializer

    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            allocation = serializer.save()
            allocation.budget.amount_allocated += allocation.amount_allocated
            allocation.budget.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)