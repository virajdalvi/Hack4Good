from django.db import models

# Create your models here.
class Info(models.Model):
    customer_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=50)
    Gst_no=models.CharField(max_length=50)
    Email_Id=models.CharField(max_length=50)
      
    def __str__(self):
        return self.Gst_no

class Product(models.Model):
    vendor_name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    GST_no=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    GST_rate=models.CharField(max_length=100)
    price=models.CharField(max_length=100)

    def __str__(self):
        return self.GST_no



