from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

STOCK_QUANTIFIERS = (
    ("kg", "Kilogram(s)"),
    ("lt", "Litre(s)"),
    ("count", "Count"),
)


class ShopStock(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="stock")
    item = models.CharField(max_length=255)
    starting_stock = models.FloatField(default=0)
    closing_stock = models.FloatField(default=0)
    quantifier = models.CharField(max_length=255, choices=STOCK_QUANTIFIERS)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
