from Hall_Admin.models import HallAdmin  # Import the HallAdmin model
from Provost.models import Provost  # Import the Provost model
from django.db import models


# Define the models for the Varsity_Admin app

class VarsityAdmin(models.Model):
    """
    Model representing a Varsity Admin.

    Attributes:
        .name (str): The name of the Varsity Admin.
        .email (str): The email address of the Varsity Admin.
        .username (str): The username of the Varsity Admin.
        .password (str): The password of the Varsity Admin.
    """

    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    username = models.CharField(max_length=100, default="NOne")
    password = models.CharField(max_length=100, default="None")

    def __str__(self):
        """
        String representation of the VarsityAdmin object.
        """
        return str(self.email)


class Hall(models.Model):
    """
    Model representing a hall in the university.

    Attributes:
        .hallId (int): The unique identifier for the hall.
        .name (str): The name of the hall.
        .hallAdmin (ForeignKey): The hall admin associated with the hall.
        .provost (ForeignKey): The provost associated with the hall.
    """

    hallId = models.IntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    hallAdmin = models.ForeignKey(HallAdmin, on_delete=models.CASCADE)
    provost = models.ForeignKey(Provost, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Hall object.
        """
        return str(self.name) + " - " + str(self.hallId)


class Room(models.Model):
    """
    Model representing a room in a hall.

    Attributes:
        .roomId (int): The unique identifier for the room.
        .capacity (int): The capacity of the room.
        .hall (ForeignKey): The hall to which the room belongs.
        .color (str): The color associated with the room.
    """

    roomId = models.IntegerField(default=0, null=True, blank=True)
    capacity = models.IntegerField(default=0, null=True, blank=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    color = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        """
        String representation of the Room object.
        """
        return str(self.roomId) + " - " + str(self.hall.hallId)