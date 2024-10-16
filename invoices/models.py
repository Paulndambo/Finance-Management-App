from django.db import models

from core.models import AbstractBaseModel
# Create your models here.
INVOICE_STATUSES = (
    ("Pending", "Pending"),
    ("Paid", "Paid"),
    ("Cancelled", "Cancelled"),
    ("Declined", "Declined"),
    ("Defaulted", "Defaulted"),
)
class Invoice(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="invoices")
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=255, null=True)
    client_address = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, choices=INVOICE_STATUSES, default="Pending")
    invoice_date = models.DateField()
    due_date = models.DateField()
    invoice_number = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.invoice_number if self.invoice_number else ""
    
    def invoice_amount(self):
        return sum(list(self.items.values_list("amount", flat=True)))
    

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=100, decimal_places=2)
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.description