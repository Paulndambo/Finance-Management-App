from django.db import models

from core.models import AbstractBaseModel
# Create your models here.
MONTH_NAMES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)
class Income(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    month = models.CharField(max_length=255, choices=MONTH_NAMES)
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.user.username} {self.month} {self.year} {self.amount}"

class IncomeRecord(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    income = models.ForeignKey(Income, on_delete=models.CASCADE)    
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
class Expenditure(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    budget = models.ForeignKey("budgets.Budget", on_delete=models.CASCADE, related_name="budgetexpenditures")
    allocation = models.ForeignKey("budgets.BudgetAllocation", on_delete=models.CASCADE, related_name="allocationexpenditures")
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.user.username