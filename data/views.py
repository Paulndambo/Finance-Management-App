from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Bill, Budget
from .serializers import BillSerializer, BudgetSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class BillViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Bill.objects.all()
        return Bill.objects.filter(user=user)

    def get_serializer_context(self):
        user = self.request.user
        return {"user": user}

class BudgetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Budget.objects.all()
        return Budget.objects.filter(user=user)

    def get_serializer_context(self):
        user = self.request.user
        return {"user": user}
