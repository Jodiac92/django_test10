from django.db import models

# Create your models here.
class MemTable(models.Model):
    memid = models.CharField(max_length=20) 
    passwd= models.CharField(max_length=20)
    name= models.CharField(max_length=20)
    email= models.CharField(max_length=40)
    phone= models.CharField(max_length=30)
    zipcode= models.CharField(max_length=20)
    address= models.CharField(max_length=100)
    job= models.CharField(max_length=20)

class ZipTab(models.Model):
    zipcode = models.CharField(max_length=7)
    area1 = models.CharField(max_length=10)
    area2 = models.CharField(max_length=20)
    area3 = models.CharField(max_length=30)
    area4 = models.CharField(max_length=50)

