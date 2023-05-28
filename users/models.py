from django.db import models
from core.models import AbstractBaseModel
from django.contrib.auth.models import User
# Create your models here.
class Profile(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.phone_number