from rest_framework import serializers
from .models import Reserve
from applications.room.serializers import RoomSerializer
from applications.customer.serializers import CustomerSerializer
from applications.hotel.serializers import HotelSerializer
from applications.room.models import Room
from applications.customer.models import Customer
from applications.hotel.models import Hotel

class ReserveSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True
    )
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True
    )
    hotel = HotelSerializer(read_only=True)
    hotel_id = serializers.PrimaryKeyRelatedField(
        queryset=Hotel.objects.all(), source='hotel', write_only=True
    )

    class Meta:
        model = Reserve
        fields = [
            'id', 'hotel', 'hotel_id', 'room', 'room_id',
            'customer', 'customer_id', 'check_in', 'check_out',
            'created_at', 'is_active'
        ]