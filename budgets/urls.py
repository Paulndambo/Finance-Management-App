from django.urls import path
from budgets.views import BudgetAllocationListCreateView

urlpatterns = [
    path("allocations/", BudgetAllocationListCreateView.as_view(), name="allocations"),
]