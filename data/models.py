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

LOAN_TYPE = (
    ("to", "Loaned To Me"),
    ("from", "From Me"),
)

LOAN_STATUS_CHOICES = (
    ("paid", "Paid"),
    ("paying", "Paying"),
    ("defaulted", "Defaulted"),
)

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    month = models.CharField(max_length=255, choices=MONTHS)
    allocated = models.DecimalField(max_digits=20, decimal_places=2)
    expenditure = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.month


class Bill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="bills")
    name = models.CharField(max_length=255)
    bill_type = models.CharField(max_length=255, choices=BILL_TYPE)
    allocated = models.DecimalField(max_digits=20, decimal_places=2)
    expenditure = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Loan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    loan_type = models.CharField(max_length=255, choices=LOAN_TYPE)
    amount_loaned = models.DecimalField(max_digits=10, decimal_places=2)
    amount_repaid = models.DecimalField(max_digits=10, decimal_places=2)
    loan_status = models.CharField(max_length=255, choices=LOAN_STATUS_CHOICES)
    loan_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

