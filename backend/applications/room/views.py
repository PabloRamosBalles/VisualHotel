from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated


from .models import Room
from .serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def rooms(request, id=None):
    print("Usuario:", request.user, "Autenticado:", request.user.is_authenticated, "Hotel:", getattr(request.user, 'hotel', None))
    print("Method:", request.method)
    if request.method == 'GET':
        user = request.user
        if user.hotel:
            rooms = Room.objects.filter(hotel=user.hotel, status='Disponible')
        else:
            rooms = Room.objects.none()
        serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PATCH':
        if not id:
            return JsonResponse({'error': 'ID requerido'}, status=400)
        try:
            room = Room.objects.get(id=id)
        except Room.DoesNotExist:
            return JsonResponse({'error': 'Room not found'}, status=404)
        data = JSONParser().parse(request)
        serializer = RoomSerializer(room, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)