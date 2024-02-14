from django.db import models
from Hall_Admin.models import HallAdmin
from Provost.models import *
from Hall_Admin.models import *
# Create your models here.
class VarsityAdmin(models.Model):
    adminId=models.IntegerField(default=0,null=True,blank=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return str(self.name)+" - "+str(self.adminId)
class Hall(models.Model):
    hallId=models.IntegerField(default=0,null=True,blank=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    hallAdmin=models.ForeignKey(HallAdmin,on_delete=models.CASCADE,null=True)
    provost=models.ForeignKey(Provost,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.name)+" - "+str(self.hallId)
class Room(models.Model):
    roomId=models.IntegerField(default=0,null=True,blank=True)
    capacity=models.IntegerField(default=0,null=True,blank=True)
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE,null=True)
    color=models.CharField(max_length=70,null=True,blank=True)
    def __str__(self):
        return str(self.roomId)+" - "+str(self.hall.hallId)