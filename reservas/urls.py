from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('reserva/', views.crear_reserva, name='crear_reserva'),
    path('reserva-exitosa/', views.reserva_exitosa, name='reserva_exitosa'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('cancelar-reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('modificar-reserva/<int:reserva_id>/', views.modificar_reserva, name='modificar_reserva'),

]