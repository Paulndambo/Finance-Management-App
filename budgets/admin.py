from django.contrib import admin
from budgets.models import Budget, BudgetAllocation


# Register your models here.
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "name",
        "year",
        "month",
        "income",
        "amount_allocated",
        "amount_spend",
        "deficit",
    ]


@admin.register(BudgetAllocation)
class BudgetAllocationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "allocation_type",
        "category",
        "budget",
        "amount_allocated",
        "amount_spend",
    ]
