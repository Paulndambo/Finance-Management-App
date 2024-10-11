from django.db import models
from core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser, AbstractBaseModel):
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=255, choices=[("Male", "Male"), ("Female", "Female")]
    )
    role = models.CharField(
        max_length=255, choices=[("Admin", "Admin"), ("User", "User")], default="User"
    )
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username

    def name(self):
        return f"{self.first_name} {self.last_name}"
