from django.db import models
class Stockinfo(models.Model):
    vendor_name=models.CharField(max_length=200)
    product_name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    quantity=models.CharField(max_length=200)
    rate=models.CharField(max_length=200)
    def __str__(self):
        return self.product_name
    


# Create your models here.
