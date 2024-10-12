from django.urls import path
from budgets.views import budgets, budget_details, new_budget, edit_budget, delete_budget, new_budget_allocation, edit_budget_allocation, delete_budget_allocation

urlpatterns = [
    path("", budgets, name="budgets"),
    path("<int:id>/details/", budget_details, name="budget-details"),
    path("new-budget/", new_budget, name="new-budget"),
    path("edit-budget/", edit_budget, name="edit-budget"),
    path("delete-budget/", delete_budget, name="delete-budget"),
    
    path("new-allocation/", new_budget_allocation, name="new-allocation"),
    path("edit-allocation/", edit_budget_allocation, name="edit-allocation"),
    path("delete-allocation/", delete_budget_allocation, name="delete-allocation"),
]
