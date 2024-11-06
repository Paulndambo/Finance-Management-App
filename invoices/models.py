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

PAYMENT_METHODS = (
    ("Mobile Money", "Mobile Money"),
    ("Bank Transfer", "Bank Transfer"),
    ("PayPal", "PayPal"),
    ("Payment Link", "Payment Link"),
)   

MOBILE_MONEY_PROVIDERS = (
    ("Mpesa Africa", "Mpesa Africa"),
    ("Airtel Money", "Airtel Money"),
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
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS, null=True)
    payment_link = models.URLField(null=True)
    
    def __str__(self):
        return self.invoice_number if self.invoice_number else ""
    
    def invoice_amount(self):
        return sum(list(self.items.values_list("amount", flat=True)))
    
    
    def invoice_link(self):
        return f"https://localhost:8000/invoices/{self.id}/details"
    

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=100, decimal_places=2)
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return self.description
    

class InvoicePaymentDetails(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, related_name="invoicepaymentdetails")
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS)
    
    bank_name = models.CharField(max_length=255, null=True)
    account_name = models.CharField(max_length=255, null=True)
    account_number = models.CharField(max_length=255, null=True)
    swift_code = models.CharField(max_length=255, null=True)
    routing_number = models.CharField(max_length=255, null=True)
    
    mobile_money_provider = models.CharField(max_length=255, choices=MOBILE_MONEY_PROVIDERS, null=True)
    mobile_money_code = models.CharField(max_length=255, null=True)
    mobile_money_name = models.CharField(max_length=255, null=True)
    mobile_money_number = models.CharField(max_length=255, null=True)
    
    paypal_email = models.EmailField(null=True)
    paypal_name = models.CharField(max_length=255, null=True)
    
    payer_name = models.CharField(max_length=255, null=True)
    payer_email = models.EmailField(null=True)
    payer_phone_number = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.invoice.invoice_number