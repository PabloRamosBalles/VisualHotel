from django.urls import path
from rest_framework.routers import DefaultRouter

# Import viewsets from each application
from applications.hotel.views import hotel_list

router = DefaultRouter()
urlpatterns = [
    path('api/hotels/', hotel_list, name='hotel-list-create'),
]