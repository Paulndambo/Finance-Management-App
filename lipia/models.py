from django.db import models

# Create your models here.
class MpesaResponseBody(models.Model):
    body = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)