from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .models import Reserve
from .serializers import ReserveSerializer

class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.hotel:
            return Reserve.objects.filter(hotel=user.hotel)
        return Reserve.objects.none()

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
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        reserve = Reserve.objects.get(id=data['id'])
        serializer = ReserveSerializer(reserve, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        reserve = Reserve.objects.get(id=data['id'])
        reserve.delete()
        return JsonResponse({'message': 'Reserve was deleted successfully!'}, status=204)