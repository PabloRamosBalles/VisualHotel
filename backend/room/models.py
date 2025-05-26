from django.db import models

# Create your models here.

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Habitación {self.number}"