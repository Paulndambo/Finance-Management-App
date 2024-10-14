from django.shortcuts import render, redirect
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from rest_framework import generics, status
from rest_framework.response import Response

from budgets.models import Budget, BudgetAllocation
from core.models import BudgetCategory
from budgets.serializers import BudgetAllocationSerializer
from finances.models import Expenditure

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
ALLOCATION_CHOICES = [
    "Rent", "Household",
    "Food", "Commuting",
    "Family", "Loan Repayments",
    "Entertainment", "Charity and Support", "Personal Use",
]


@login_required(login_url="/users/login")
def budgets(request):
    budgets = Budget.objects.filter(user=request.user).order_by("-created")

    total_allocated = sum(list(Budget.objects.filter(user=request.user).values_list("amount_allocated", flat=True)))
    total_budgeted = sum(list(BudgetAllocation.objects.filter(user=request.user).values_list("amount_allocated", flat=True)))
    total_spend = sum(list(Expenditure.objects.filter(user=request.user).values_list("amount", flat=True)))
    

    paginator = Paginator(budgets, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "total_allocated": total_allocated,
        "total_budgeted": total_budgeted,
        "total_spend": total_spend,
        "years": years_list,
        "months": months_list,
        "allocation_types": ALLOCATION_CHOICES,
    }
    return render(request, "budgets/budgets.html", context)


@login_required(login_url="/users/login")
def budget_details(request, id):
    allocations = BudgetAllocation.objects.filter(budget_id=id).order_by("-created")

    budget = Budget.objects.get(id=id)
    
    total_spend = sum(list(Expenditure.objects.filter(user=request.user, budget=budget).values_list("amount", flat=True)))
    
    total_budgeted = allocations.aggregate(total_budgeted=Sum('amount_allocated'))["total_budgeted"]
    
    budget_categories = BudgetCategory.objects.all()

    paginator = Paginator(allocations, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "allocated": budget.amount_allocated,
        "budgeted": total_budgeted if total_budgeted else 0,
        "allocation_types": ALLOCATION_CHOICES,
        "total_spend": total_spend,
        "budget": budget,
        "balance": total_budgeted - total_spend,
        "budget_categories": budget_categories
    }
    return render(request, "budgets/budget_details.html", context)


@login_required(login_url="/users/login")
def new_budget(request):
    if request.method == "POST":
        budget = Budget.objects.create(
            user=request.user,
            month=request.POST.get("month"),
            year=int(request.POST.get("year")),
            amount_allocated=request.POST.get("amount_allocated"),
        )
        return redirect("budgets")
    return render(request, "budgets/new_budget.html")


@login_required(login_url="/users/login")
def edit_budget(request):
    if request.method == "POST":
        id = request.POST.get("budget_id")
        budget = Budget.objects.get(id=id)
        budget.month = request.POST.get("month")
        budget.year = int(request.POST.get("year"))
        budget.amount_allocated=request.POST.get("amount_allocated")
        budget.save()
        return redirect("budgets")
    return render(request, "budgets/edit_budget.html")


@login_required(login_url="/users/login")
def delete_budget(request):
    if request.method == "POST":
        id = request.POST.get("budget_id")
        budget = Budget.objects.get(id=id)
        budget.delete()
        return redirect("budgets")
    return render(request, "budgets/delete_budget.html")


@login_required(login_url="/users/login")
def new_budget_allocation(request):
    if request.method == "POST":
        budget_allocation = BudgetAllocation.objects.create(
            user=request.user,
            budget_id=request.POST.get("budget_id"),
            allocation_type=request.POST.get("allocation_type"),
            amount_allocated=request.POST.get("amount_allocated"),
        )
        return redirect(f"/budgets/{budget_allocation.budget.id}/details")
    return render(request, "budgets/allocations/new_allocation.html")



@login_required(login_url="/users/login")
def edit_budget_allocation(request):
    if request.method == "POST":
        id = request.POST.get("allocation_id")
        budget_allocation = BudgetAllocation.objects.get(id=id)    
        budget_allocation.allocation_type = request.POST.get("allocation_type")
        budget_allocation.amount_allocated = request.POST.get("amount_allocated")
        budget_allocation.save()
        return redirect("budgets")
    return render(request, "budgets/allocations/edit_allocation.html")


@login_required(login_url="/users/login")
def delete_budget_allocation(request):
    if request.method == "POST":
        id = request.POST.get("allocation_id")
        budget_allocation = BudgetAllocation.objects.get(id=id)
        budget_allocation.delete()
        return redirect("budgets")
    return render(request, "budgets/allocations/delete_allocation.html")