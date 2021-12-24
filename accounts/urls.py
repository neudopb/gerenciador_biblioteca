from django.urls import path, include
from accounts.views import UsuarioCreateAPIView, UsuarioListAPIView

urlpatterns = [
    path('api/', UsuarioCreateAPIView.as_view()),
    path('api/list/', UsuarioListAPIView.as_view()),
]