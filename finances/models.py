from django.db import models

from core.models import AbstractBaseModel
# Create your models here.
class Expenditure(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    budget = models.ForeignKey("budgets.Budget", on_delete=models.CASCADE, related_name="budgetexpenditures")
    allocation = models.ForeignKey("budgets.BudgetAllocation", on_delete=models.CASCADE, related_name="allocationexpenditures")
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.user.username