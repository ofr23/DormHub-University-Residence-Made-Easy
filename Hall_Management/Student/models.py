from django.db import models
from Varsity_Admin.models import Hall, Room


class Session(models.Model):
    """
    Model representing a session.

    A session represents a specific academic term or period.

    Attributes:
        .session (int): The session number.
        .csvFile (FileField): The CSV file associated with this session.
    """

    session = models.IntegerField(default=0, null=True, blank=True)
    csvFile = models.FileField(upload_to='csvs/', null=True, blank=True)

    def __str__(self):
        """String representation of the session."""
        return str(self.session)


class Student(models.Model):
    """
    Model representing a student.

    A student is a person enrolled in a particular session, hall, and room.

    Attributes:
        .studentId (int): The unique identifier for the student.
        .name (str): The name of the student.
        .email (str): The email address of the student.
        .username (str): The username of the student.
        .password (str): The password of the student.
        .hall (ForeignKey): The hall the student belongs to.
        .session (ForeignKey): The session the student is enrolled in.
        .room (ForeignKey): The room the student is assigned to.
        .studentType (str): The type of student (e.g., undergraduate, graduate).
    """

    studentId = models.IntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    studentType = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """String representation of the student."""
        return f"{self.name} - {self.studentId}"
class SwapRequest(models.Model):
    student=models.ForeignKey(Student,null=True,on_delete=models.CASCADE)
    reason=models.CharField(max_length=200,null=True)
    status=models.IntegerField(default=0,null=True)
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.student.studentId)+" - "+str(self.hall.hallId)
class RepairRequest(models.Model):
    student=models.ForeignKey(Student,null=True,on_delete=models.CASCADE)
    reason=models.CharField(max_length=200,null=True)
    status=models.IntegerField(default=0,null=True)
    hall=models.ForeignKey(Hall,on_delete=models.CASCADE,null=True)
    requestType=models.IntegerField(default=0,null=True)
    def __str__(self):
        return str(self.student.studentId)+" - "+str(self.hall.hallId)