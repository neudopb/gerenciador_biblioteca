from django.urls import path
from livro import views

urlpatterns = [
    path('api/', views.LivrosListCreateAPIView.as_view()),
    path('api/<int:pk>/', views.LivrosRetrieveUpdateDestroyAPIView.as_view()),
    path('genero/api/', views.GeneroListCreateAPIView.as_view()),
    path('genero/api/<int:pk>/', views.GeneroRetrieveUpdateDestroyAPIView.as_view()),
]