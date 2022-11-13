from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Bill, Budget
from .serializers import BillSerializer, BudgetSerializer
# Create your views here.
class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer