from django.db import models
from room.models import Room
from customer.models import Customer

# Create your models here.

class Reserve(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva {self.id} - Habitación {self.room.number}"