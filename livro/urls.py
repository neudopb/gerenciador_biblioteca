from django.urls import path
from livro.views import GeneroListCreateAPIView, GeneroRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('genero/api/', GeneroListCreateAPIView.as_view()),
    path('genero/api/<int:pk>/', GeneroRetrieveUpdateDestroyAPIView.as_view()),
]