from django.db import models

# Create your models here.
class Destination(models.Model) :
    username = models.CharField(max_length = 10)
    pswd = models.CharField(max_length = 10)