from django.db import models
class Provost(models.Model):
    provostId=models.IntegerField(default=1,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(unique=True,max_length=100)
    username=models.CharField(max_length=100,default="None")
    password=models.CharField(max_length=100,default="None")
    def __str__(self):
        return str(self.email)