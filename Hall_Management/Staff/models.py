from django.db import models
from Varsity_Admin.models import *
# Create your models here.
class Staff(models.Model):
    staffId=models.IntegerField(default=0,null=True,blank=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.name)+" - "+str(self.staffId)
class Visitor(models.Model):
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE,null=True)
    visitorId=models.IntegerField(default=0,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    visit=models.CharField(max_length=100,null=True,blank=True)
    arrival=models.TimeField(null=True,blank=True)
    departure=models.TimeField(null=True,blank=True)
    def __str__(self):
        return str(self.date)+" - "+str(self.visitorId)
