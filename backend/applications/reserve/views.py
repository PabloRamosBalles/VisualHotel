from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Reserve
from .serializers import ReserveSerializer

class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer