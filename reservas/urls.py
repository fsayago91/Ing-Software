from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('reserva/', views.crear_reserva, name='crear_reserva'),
    path('reserva-exitosa/', views.reserva_exitosa, name='reserva_exitosa'),
]