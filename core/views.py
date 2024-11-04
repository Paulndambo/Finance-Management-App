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
        list(Expenditure.objects.filter(user=user).values_list("amount", flat=True))
    )
    

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
    
    expenditures = Expenditure.objects.filter(user=user).order_by("-created")[:5]

    context = {
        "income": income,
        "total_budget": total_budgeted,
        "total_spend": total_spend,
        "loans_total": loans_total,
        "total_investments": investments,
        "expenditures": expenditures
    }

    return render(request, "dashboard.html", context)

def index(request):
    return render(request, "dashboard1.html")