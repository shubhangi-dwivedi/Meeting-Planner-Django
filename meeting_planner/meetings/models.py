from tkinter.constants import CASCADE

from django.db import models
from datetime import time

class Room(models.Model):
    room = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.room} at {self.floor} on {self.room_number}"


# Create your models here.
class Meeting(models.Model):
    title =  models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    #foreign key
    #this will help us select the room when we create a meeting
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #this will hold the ID of the room obj that the meeting ref

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

