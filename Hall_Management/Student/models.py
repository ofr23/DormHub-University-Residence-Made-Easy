from django.db import models
from Hall_Admin.models import *
# Create your models here.from django.db import models
class Session(models.Model):
    session=models.IntegerField(default=0,null=True,blank=True)
    csvFile=models.FileField(upload_to='csvs/',null=True,blank=True)
    def __str__(self):
        return str(self.session)
    
class Student(models.Model):
    residentId=models.IntegerField(default=0,null=True,blank=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE,null=True)
    session=models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return str(self.name)+" - "+str(self.studentId)