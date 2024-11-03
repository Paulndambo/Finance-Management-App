from django.db import models

from core.models import AbstractBaseModel
# Create your models here.
class ChimmoneyPaymentRequest(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    payment_reference = models.CharField(max_length=255, null=True)
    payer_name = models.CharField(max_length=255, null=True)
    payment_id = models.CharField(max_length=255, null=True)
    payment_link = models.CharField(max_length=255, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=255)
    payer_email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    
class ChimmoneyPayout(AbstractBaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    payment_reference = models.CharField(max_length=255, null=True)
    