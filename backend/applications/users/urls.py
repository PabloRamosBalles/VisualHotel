from django.urls import path
from .views import LoginView

from applications.users import views
urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
]