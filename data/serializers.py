from rest_framework import serializers
from .models import Budget, Bill

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['user']
        return Bill.objects.create(user=user, **validated_data)

class BudgetSerializer(serializers.ModelSerializer):
    total_bills = serializers.SerializerMethodField(read_only=True)
    budget_distribution = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Budget
        fields = ["id", "user", "month", "allocated",
                  "expenditure", "total_bills", "budget_distribution", "created", "modified"]


    def create(self, validated_data):
        user = self.context['user']
        return Budget.objects.create(user=user, **validated_data)

    def get_total_bills(self, obj):
        total_allocated = sum(obj.bills.values_list('allocated', flat=True))
        total_spend = sum(obj.bills.values_list('expenditure', flat=True))
        return {
            "total_budgeted": total_allocated,
            "total_spend": total_spend
        }

    def get_budget_distribution(self, obj):
        investment = sum(obj.bills.filter(bill_type="investment").values_list('allocated', flat=True))
        basic = sum(obj.bills.filter(bill_type="basic").values_list('allocated', flat=True))
        luxury = sum(obj.bills.filter(bill_type="luxury").values_list('allocated', flat=True))
        family = sum(obj.bills.filter(bill_type="family").values_list('allocated', flat=True))
        other_bills = sum(obj.bills.filter(bill_type="family").values_list('allocated', flat=True))
        return {
            "basic_needs": basic,
            "family": family,
            "luxury": luxury,
            "other_bills": other_bills,
            "investment": investment
        }
