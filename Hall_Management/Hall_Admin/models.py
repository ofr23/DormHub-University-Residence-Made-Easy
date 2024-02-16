from django.db import models
from Provost.models import *
from Varsity_Admin.models import *
# Create your models here.

class HallAdmin(models.Model):
    adminId=models.IntegerField(default=1,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(unique=True,max_length=100)
    username=models.CharField(max_length=100,default="")
    password=models.CharField(max_length=100,default="")
    def __str__(self):
        return str(self.email)