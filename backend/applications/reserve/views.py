from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from datetime import date

from applications.customer.models import Customer
from applications.room.models import Room

from .models import Reserve
from .serializers import ReserveSerializer

class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.hotel:
            reservas = Reserve.objects.filter(hotel=user.hotel, is_active=True)
            rooms = Room.objects.filter(hotel=user.hotel)
            for room in rooms:
                update_room_status(room)
            return reservas
        return Reserve.objects.none()
    
    def create(self, request, *args, **kwargs):
        customer_data = request.data.get('customer')
        room_id = request.data.get('room')
        hotel_id = request.data.get('hotel')
        check_in = request.data.get('check_in')
        check_out = request.data.get('check_out')

        customer = Customer.objects.create(**customer_data)
        room = Room.objects.get(id=room_id)

        reserve = Reserve.objects.create(
            hotel_id=hotel_id,
            room=room,
            customer=customer,
            check_in=check_in,
            check_out=check_out
        )
        update_room_status(room)
        serializer = self.get_serializer(reserve)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        print("BORRANDO RESERVA")
        instance = self.get_object()
        room = instance.room
        # self.perform_destroy(instance)
        instance.is_active = False
        instance.save()
        update_room_status(room)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, request, *args, **kwargs):
        print(request.data)
        instance = self.get_object()
        old_room = instance.room 
        response = super().partial_update(request, *args, **kwargs)
        instance.refresh_from_db()

        update_room_status(old_room)
        update_room_status(instance.room)
        return response

def update_room_status(room):
    today = date.today()
    # ¿Hay alguna reserva activa para esta habitación en curso o futura?
    reservas_activas = Reserve.objects.filter(
        room=room,
        is_active=True,
        check_out__gt=today
    )
    if reservas_activas.exists():
        if room.status != 'Ocupada':
            room.status = 'Ocupada'
            room.save()
    else:
        if room.status != 'Disponible':
            room.status = 'Disponible'
            room.save()

@csrf_exempt
def reserve_list(request):
    if request.method == 'GET':
        reserves = Reserve.objects.all()
        serializer = ReserveSerializer(reserves, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReserveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    # elif request.method == 'PATCH':
    #     data = JSONParser().parse(request)
    #     reserve = Reserve.objects.get(id=data['id'])
    #     serializer = ReserveSerializer(reserve, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        reserve = Reserve.objects.get(id=data['id'])
        reserve.is_active = False
        reserve.save()
        return JsonResponse({'message': 'Reserve was deleted successfully!'}, status=204)