from django.db import models

class Provost(models.Model):
    """
    Model representing a Provost.

    Attributes:
        provostId (int): The unique identifier for the provost.
        name (str): The name of the provost.
        email (str): The email address of the provost (unique).
        username (str): The username of the provost.
        password (str): The password of the provost.
    """
    
    provostId = models.IntegerField(default=1, null=True)  # Field for Provost ID
    name = models.CharField(max_length=100, blank=True, null=True)  # Field for Provost name
    email = models.EmailField(unique=True, max_length=100)  # Field for Provost email (unique)
    username = models.CharField(max_length=100, default="None")  # Field for Provost username
    password = models.CharField(max_length=100, default="None")  # Field for Provost password

    def __str__(self):
        """
        String representation of the Provost object.

        Returns:
            str: The email address of the provost.
        """
        return str(self.email)
