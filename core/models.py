from django.db import models

# Create your models here.
class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BudgetCategory(AbstractBaseModel):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name