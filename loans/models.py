from django.db import models

from core.models import AbstractBaseModel
# Create your models here.
LOAN_TYPES = (
    ("Given Out", "Given Out"),
    ("Received", "Received"),
)

PAYMENT_METHODS = (
    ("Cash", "Cash"),
    ("Card", "Card"),
    ("Cheque", "Cheque"),
    ("Bank Transfer", "Bank Transfer"),
    ("Mpesa", "Mpesa"),
    ("Other", "Other"),
)

class Loan(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    given_by = models.CharField(max_length=255, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_to_repay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duration = models.IntegerField()
    installment = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    date_due = models.DateField(null=True)
    loan_type = models.CharField(max_length=255, choices=LOAN_TYPES, null=True)
    fully_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def loan_balance(self):
        return self.amount_to_repay - self.amount_paid
    
    

class LoanRepayment(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="loanrepayments")
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS, default="Mpesa")
  
    def __str__(self):
        return self.loan.user.username