from django.shortcuts import render
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from rest_framework import generics, status
from rest_framework.response import Response

from budgets.models import Budget, BudgetAllocation
from budgets.serializers import BudgetAllocationSerializer

# Create your views here.

months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
years_list = [2024, 2025, 2026, 2028, 2029, 2030]


@login_required(login_url="/users/login")
def budgets(request):
    budgets = Budget.objects.all().order_by("-created")

    total_budgeted = sum(
        list(Budget.objects.values_list("amount_allocated", flat=True))
    )
    total_spend = sum(list(Budget.objects.values_list("amount_spend", flat=True)))
    balance = total_budgeted - total_spend

    income = sum(list(Budget.objects.values_list("income", flat=True)))
    print(f"Income: {income}")

    paginator = Paginator(budgets, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "total_budgeted": total_budgeted,
        "total_spend": total_spend,
        "balance": balance,
        "income": income,
        "years": years_list,
        "months": months_list,
    }
    return render(request, "budgets/budgets.html", context)


@login_required(login_url="/users/login")
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
        "balance": budget.amount_allocated - budget.amount_spend,
    }
    return render(request, "budgets/allocations.html", context)


def new_budget(request):
    if request.method == "POST":
        pass
