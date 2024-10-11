from rest_framework import serializers
from budgets.models import BudgetAllocation


class BudgetAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetAllocation
        fields = "__all__"
