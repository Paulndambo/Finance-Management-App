from django.urls import path
from budgets.views import budgets, budget_allocations

urlpatterns = [
    path("", budgets, name="budgets"),
    path("allocations/<int:id>/", budget_allocations, name="allocations"),
]
