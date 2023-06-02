from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Bill, Budget
from .serializers import BillSerializer, BudgetSerializer, BillUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.
class BillViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                return Bill.objects.all()
            return Bill.objects.filter(user=user)
        return Response({"message": "Please Login"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_serializer_context(self):
        user = self.request.user
        return {"user": user}
    

class BillUpdateAPIView(generics.CreateAPIView):
    serializer_class = BillUpdateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            try:
                amount_spend = data.get("amount_spend")
                bill = Bill.objects.get(id=data.get("bill"))

                if request.user == bill.user:
                    allocated = bill.allocated
                    expenditure = bill.expenditure
                    total_expenditure = expenditure + amount_spend
                    new_amount_saved = allocated - total_expenditure
                    bill.amount_saved = new_amount_saved
                    bill.expenditure = total_expenditure
                    bill.save()
                else:
                    return Response({"failed": "You can only update your own bills"}, status=status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                raise e

            print(f"Bill: {bill}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class BudgetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                return Budget.objects.all()
            return Budget.objects.filter(user=user)
        return Response({"message": "Please Login!!"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_serializer_context(self):
        user = self.request.user
        return {"user": user}


