from django.urls import path
from emprestimo import views

urlpatterns = [
    path('api/', views.EmprestimoListCreateAPIView.as_view()),
    path('api/<int:pk>/', views.EmprestimoRetrieveUpdateDestroyAPIView.as_view()),
    path('api/finalizar/<int:pk>/', views.EmprestimoDevolver.as_view()),
]