from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from budgets.models import Budget, BudgetAllocation
from loans.models import Loan
from finances.models import Expenditure, Income, Investment


# Create your views here.
@login_required(login_url="/users/login")
def dashboard(request):
    user = request.user
    total_budgeted = sum(
        list(
            BudgetAllocation.objects.filter(user=user).values_list("amount_allocated", flat=True)
        )
    )
    total_spend = sum(
        list(BudgetAllocation.objects.filter(user=user).values_list("amount_spend", flat=True))
    )
    balance = total_budgeted - total_spend

    income = sum(
        list(Income.objects.filter(user=user).values_list("amount", flat=True))
    )

    loans_total = sum(
        list(Loan.objects.filter(user=user).values_list("amount_to_repay", flat=True))
    )
    investments = sum(
        list(
            Investment.objects.filter(user=user)
            .values_list("amount", flat=True)
            .order_by("-created")
        )
    )

    context = {
        "income": income,
        "total_budget": total_budgeted,
        "total_spend": total_spend,
        "loans_total": loans_total,
        "total_investments": investments,
    }

    return render(request, "dashboard.html", context)
