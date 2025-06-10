from django.db import models
from applications.hotel.models import Hotel
from applications.room.models import Room
from applications.customer.models import Customer

# Create your models here.

class Reserve(models.Model):
    id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Reserva {self.id} - Habitación {self.room.number}"