from django.shortcuts import render
from django.db import transaction
from django.core.paginator import Paginator

from rest_framework import generics, status
from rest_framework.response import Response

from budgets.models import Budget, BudgetAllocation
from budgets.serializers import BudgetAllocationSerializer
# Create your views here.    
def budgets(request):
    budgets = Budget.objects.all().order_by("-created")

    total_budgeted = sum(list(Budget.objects.values_list("amount_allocated", flat=True)))
    total_spend = sum(list(Budget.objects.values_list("amount_spend", flat=True)))
    balance = total_budgeted - total_spend

    income = sum(list(Budget.objects.values_list("income", flat=True)))
    print(f"Income: {income}")

    paginator = Paginator(budgets, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "total_budgeted": total_budgeted,
        "total_spend": total_spend,
        "balance": balance,
        "income": income
    }
    return render(request, "budgets/budgets.html", context)


def budget_allocations(request, id):
    allocations = BudgetAllocation.objects.filter(budget_id=id).order_by("-created")

    budget = Budget.objects.get(id=id)

    paginator = Paginator(allocations, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "allocated": budget.amount_allocated,
        "spend": budget.amount_spend,
        "income": budget.income,
        "balance": budget.amount_allocated - budget.amount_spend
    }
    return render(request, "budgets/allocations.html", context)


"""
@transaction.atomic
def budgets(request):
    data = request.data
    serializer = self.serializer_class(data=data)

    if serializer.is_valid(raise_exception=True):
        allocation = serializer.save()
        allocation.budget.amount_allocated += allocation.amount_allocated
        allocation.budget.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""