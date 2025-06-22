from django.db import models
from django.contrib.auth.models import User

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)  # Ej: sintética, césped natural
    estado = models.CharField(max_length=50, choices=[
        ('disponible', 'Disponible'),
        ('mantenimiento', 'En mantenimiento'),
        ('fuera', 'Fuera de servicio'),
    ])

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
    

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.usuario.username} - {self.cancha.nombre} - {self.fecha} {self.hora}"

