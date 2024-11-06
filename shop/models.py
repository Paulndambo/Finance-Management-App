from django.db import models

from core.models import AbstractBaseModel
# Create your models here.

class Product(AbstractBaseModel):
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    

class ProductImage(AbstractBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    
    def __str__(self):
        return self.product.name
