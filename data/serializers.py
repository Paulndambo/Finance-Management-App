from rest_framework import serializers
from .models import Budget, Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['user']
        return Bill.objects.create(user=user, **validated_data)
    
    def update(self, instance, validated_data):
        expenditure = validated_data.get("expenditure")
        allocated = validated_data.get("allocated")
        name = validated_data.get("name")
        amount_saved = allocated - expenditure
        instance.allocated = allocated
        instance.expenditure = expenditure
        instance.name = name
        instance.amount_saved = amount_saved
        instance.save()
        return instance
    
    
class BillUpdateSerializer(serializers.Serializer):
    amount_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    bill = serializers.IntegerField()


class BudgetSerializer(serializers.ModelSerializer):
    total_bills = serializers.SerializerMethodField(read_only=True)
    budget_distribution = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Budget
        fields = ["id", "user", "month", "year", "allocated",
                  "expenditure", "total_bills", "budget_distribution", "created", "modified"]


    def create(self, validated_data):
        user = self.context['user']
        return Budget.objects.create(user=user, **validated_data)


    def get_total_bills(self, obj):
        total_allocated = sum(obj.bills.values_list('allocated', flat=True))
        total_spend = sum(obj.bills.values_list('expenditure', flat=True))
        budget_diff = total_allocated - total_spend
        budget_deficit = total_allocated - obj.allocated 
        return {
            "budget_allocation": obj.allocated,
            "total_budgeted_amount": total_allocated,
            "total_spend": total_spend,
            "amount_saved": budget_diff,
            "budget_deficit": budget_deficit
        }

    def get_budget_distribution(self, obj):
        investment = sum(obj.bills.filter(bill_type="investment").values_list('allocated', flat=True))

        basic_needs_exp = sum(obj.bills.filter(bill_type="basic").values_list('expenditure', flat=True))
        basic_needs_allocation = sum(obj.bills.filter(bill_type="basic").values_list('allocated', flat=True))
        basic_needs_savings = basic_needs_allocation - basic_needs_exp #sum(obj.bills.filter(bill_type="basic").values_list('amount_saved', flat=True))

        luxury_exp = sum(obj.bills.filter(bill_type="luxury").values_list('expenditure', flat=True))
        luxury_allocation = sum(obj.bills.filter(bill_type="luxury").values_list('allocated', flat=True))
        luxury_savings = luxury_allocation - luxury_exp #sum(obj.bills.filter(bill_type="luxury").values_list('amount_saved', flat=True))

        family_exp = sum(obj.bills.filter(bill_type="family").values_list('expenditure', flat=True))
        family_allocation = sum(obj.bills.filter(bill_type="family").values_list('allocated', flat=True))
        family_savings = family_allocation - family_exp #sum(obj.bills.filter(bill_type="family").values_list('amount_saved', flat=True))

        other_bills_allocated = sum(obj.bills.filter(bill_type="other").values_list('allocated', flat=True))
        other_bills_expenditure = sum(obj.bills.filter(bill_type="other").values_list('expenditure', flat=True))
        other_bills_savings = other_bills_allocated - other_bills_expenditure #sum(obj.bills.filter(bill_type="other").values_list('amount_saved', flat=True))
        return {
            "basic_needs": {
                "expediture": basic_needs_exp,
                "allocation": basic_needs_allocation,
                "savings": basic_needs_savings
            },
            "family": {
                "expenditure": family_exp,
                "allocation": family_allocation,
                "savings": family_savings
            },
            "luxury": {
                "expenditure": luxury_exp,
                "allocation": luxury_allocation,
                "savings": luxury_savings
            },
            "other_bills": {
                "expenditure": other_bills_expenditure,
                "allocation": other_bills_allocated,
                "savings": other_bills_savings
            },
            "investment": investment
        }
