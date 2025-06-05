from rest_framework import serializers
from .models import Reserve
from applications.room.serializers import RoomSerializer
from applications.customer.serializers import CustomerSerializer
from applications.hotel.serializers import HotelSerializer

class ReserveSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    customer = CustomerSerializer()
    hotel = HotelSerializer()
    class Meta:
        model = Reserve
        fields = '__all__'