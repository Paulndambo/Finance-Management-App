from django.db.models import F, Sum
from data.models import Budget, Bill


def match_budget_amounts():
    budgets = Budget.objects.filter(allocated__gt=F('expenditure'))
    for budget in budgets:
        amount_spend = sum(budget.bills.values_list('expenditure', flat=True))
        amount_saved = budget.allocated - amount_spend
        budget.amount_saved = amount_saved
        budget.expenditure = amount_spend
        budget.save()
        