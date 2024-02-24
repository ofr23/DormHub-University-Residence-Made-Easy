from django.db import models


class Provost(models.Model):
    provostId = models.IntegerField(default=1, null=True)  # Field for Provost ID
    name = models.CharField(max_length=100, blank=True, null=True)  # Field for Provost name
    email = models.EmailField(unique=True, max_length=100)  # Field for Provost email (unique)
    username = models.CharField(max_length=100, default="None")  # Field for Provost username
    password = models.CharField(max_length=100, default="None")  # Field for Provost password

    def __str__(self):
        return str(self.email)
