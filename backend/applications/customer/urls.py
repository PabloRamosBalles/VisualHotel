from django.urls import path
from rest_framework.routers import DefaultRouter

# Import viewsets from each application
from applications.customer import views

router = DefaultRouter()
urlpatterns = [
    path('api/customers/', views.customer_list, name='customer-list-create'),
]