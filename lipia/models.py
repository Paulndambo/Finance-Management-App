from django.db import models
from core.models import AbstractBaseModel
# Create your models here.
class MpesaResponseBody(AbstractBaseModel):
    body = models.JSONField()


class MpesaTransaction(AbstractBaseModel):
    receipt_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    merchant_request_id = models.CharField(max_length=255)
    checkout_request_id = models.CharField(max_length=255)
    transaction_result_code = models.CharField(max_length=255)
    transaction_timestamp = models.FloatField()

    def __str__(self):
        return self.phone_number + " has paid " + str(self.amount)
    

BILL_NUMBER_TYPE_CHOICES = (
    ("till_number", "Till Number"),
    ("paybill_number", "Paybill Number"),
)


class ServiceProvider(AbstractBaseModel):
    name = models.CharField(max_length=255)
    services = models.JSONField(null=True, blank=True)
    bill_number = models.CharField(max_length=255)
    bill_number_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name