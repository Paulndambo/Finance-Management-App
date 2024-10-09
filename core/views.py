from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from budgets.models import Budget, BudgetAllocation
# Create your views here.
@login_required(login_url="/users/login")
def dashboard(request):
    total_budgeted = sum(list(Budget.objects.values_list("amount_allocated", flat=True)))
    total_spend = sum(list(Budget.objects.values_list("amount_spend", flat=True)))
    balance = total_budgeted - total_spend

    income = sum(list(Budget.objects.values_list("income", flat=True)))

    context = {
        "income": income,
        "total_budget": total_budgeted,
        "total_spend": total_spend
    }

    return render(request, 'dashboard.html', context)