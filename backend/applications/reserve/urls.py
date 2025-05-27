from django.urls import path
from rest_framework.routers import DefaultRouter

# Import viewsets from each application
from applications.reserve import views

router = DefaultRouter()
urlpatterns = [
    path('api/reserves/', views.reserve_list, name='reserve-list-create'),
]