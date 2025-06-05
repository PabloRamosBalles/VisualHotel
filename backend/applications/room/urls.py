from django.urls import path
from rest_framework.routers import DefaultRouter

# Import viewsets from each application
from applications.room import views

router = DefaultRouter()
urlpatterns = [
    path('api/rooms/', views.rooms, name='room-list-create'),
]