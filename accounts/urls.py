from django.urls import path, include
from .api import viewsets
from . import views

urlpatterns = [
    path('api/', viewsets.UsuarioCreateAPIView.as_view()),
    path('api/list/', viewsets.UsuarioListAPIView.as_view()),
]