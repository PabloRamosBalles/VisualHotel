from django.db import models

from applications.hotel.models import Hotel

# Create your models here.

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Habitación {self.number}"