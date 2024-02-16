from django.db import models
from Varsity_Admin.models import *
import datetime
# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(unique=True,max_length=100)
    username=models.CharField(max_length=100,default='')
    password=models.CharField(max_length=100,default='')
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.email)
class Visitor(models.Model):
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE)
    visitorId=models.IntegerField(default=0,null=True,blank=True)
    date=models.DateField(default=datetime.datetime.now().date())
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    visit=models.CharField(max_length=100,null=True,blank=True)
    arrival=models.TimeField(null=True,blank=True)
    departure=models.TimeField(null=True,blank=True)
    def __str__(self):
        return str(self.date)+" - "+str(self.visitorId)
