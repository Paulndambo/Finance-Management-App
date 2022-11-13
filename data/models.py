from django.db import models
from django.conf import settings

# Create your models here.
MONTHS = (
    ("january", "January"),
    ("february", "February"),
    ("march", "March"),
    ("april", "April"),
    ("may", "May"),
    ("june", "June"),
    ("july", "July"),
    ("august", "August"),
    ("september", "September"),
    ("october", "October"),
    ("november", "November"),
    ("december", "December"),
)

BILL_TYPE = (
    ("basic", "Basic"),
    ("family", "Family"),
    ("luxury", "Luxury"),
    ("investment", "Investment"),
    ("other", "Other"),
)

class Budget(models.Model):
    month = models.CharField(max_length=255, choices=MONTHS)
    allocated = models.DecimalField(max_digits=20, decimal_places=2)
    expenditure = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.month


class Bill(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="bills")
    name = models.CharField(max_length=255)
    bill_type = models.CharField(max_length=255, choices=BILL_TYPE)
    allocated = models.DecimalField(max_digits=20, decimal_places=2)
    expenditure = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
