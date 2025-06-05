from django.urls import path
from rest_framework.routers import DefaultRouter

# Import viewsets from each application
from applications.reserve import views

router = DefaultRouter()
urlpatterns = [
    path('api/all/reserves/', views.reserve_list, name='reserve-list-create'),
    path('api/reserves/', views.ReserveViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('api/reserves/<int:pk>/',views.ReserveViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]