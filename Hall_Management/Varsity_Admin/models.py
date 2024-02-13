from django.db import models

# Create your models here.
class VarsityAdmin(models.Model):
    adminId=models.IntegerField(default=0,null=True,blank=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    username=models.CharField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return str(self.name)+" - "+str(self.adminId)