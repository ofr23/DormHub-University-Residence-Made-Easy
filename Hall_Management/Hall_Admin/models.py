from django.db import models


class HallAdmin(models.Model):
    """
    Model representing a Hall Admin.
    """
    adminId = models.IntegerField(default=1, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        """
        String representation of the HallAdmin object.
        """
        return str(self.email)
