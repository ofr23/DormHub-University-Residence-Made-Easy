from django.db import models
from Provost.models import *
# Create your models here.
# class HallAdmin(models.Model):
#     name=models.CharField(max_length=100,blank=True,null=True)
#     email=models.EmailField(max_length=100,blank=True,null=True)
#     username=models.CharField(max_length=100,blank=True,null=True)
#     password=models.CharField(max_length=100,blank=True,null=True)

# class Hall(models.Model):
#     name=models.CharField(max_length=100,blank=True,null=True)
#     hallAdmin=models.ForeignKey(HallAdmin,on_delete=models.CASCADE,null=True,blank=True)
#     provost=models.ForeignKey(Provost,on_delete=models.CASCADE,null=True,blank=True)
#     def __str__(self):
