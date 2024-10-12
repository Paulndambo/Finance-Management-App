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

ALLOCATION_CHOICES = (
    ("Rent", "Rent"),
    ("Household", "Household"),
    ("Food", "Food"),
    ("Commuting", "Commuting"),
    ("Family", "Family"),
    ("Entertainment", "Entertainment"),
    ("Charity and Support", "Charity and Support"),
    ("Personal Use", "Personal Use"),
)


class Budget(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    amount_allocated = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    deficit = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    year = models.IntegerField()
    month = models.CharField(max_length=255, choices=MONTH_NAMES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def amount_budgeted(self):
        allocations = self.budgetallocations.all().values_list("amount_allocated", flat=True)
        return sum(allocations)
        
    def amount_spend(self):
        allocations = self.budgetallocations.all().values_list("amount_spend", flat=True)
        return sum(allocations)


class BudgetAllocation(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    allocation_type = models.CharField(max_length=255, choices=ALLOCATION_CHOICES, null=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="budgetallocations")
    category = models.ForeignKey("core.BudgetCategory", on_delete=models.SET_NULL, null=True)
    amount_allocated = models.DecimalField(max_digits=100, decimal_places=2)
    amount_spend = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return self.budget.name
