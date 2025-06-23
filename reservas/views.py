from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReservaForm
from .models import Reserva
from django.shortcuts import get_object_or_404
from .forms import ModificarReservaForm
from datetime import date
from .models import Cancha
from django.contrib.auth.models import Group

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Asignar al grupo "cliente" automáticamente
            grupo_cliente, creado = Group.objects.get_or_create(name='cliente')
            user.groups.add(grupo_cliente)

            messages.success(request, "Usuario registrado exitosamente. Ahora podés iniciar sesión.")
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'reservas/registro.html', {'form': form})

@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user  # Asigna el usuario logueado
            reserva.save()
            return redirect('reserva_exitosa')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})

def reserva_exitosa(request):
    return render(request, 'reservas/reserva_exitosa.html')

@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by('fecha', 'hora')
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})

@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    reserva.delete()
    return redirect('mis_reservas')

from .forms import ModificarReservaForm

@login_required
def modificar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    if request.method == 'POST':
        form = ModificarReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('mis_reservas')
    else:
        form = ModificarReservaForm(instance=reserva)
    return render(request, 'reservas/modificar_reserva.html', {'form': form})

@login_required
def historial_reservas(request):
    historial = Reserva.objects.filter(usuario=request.user).order_by('-fecha', '-hora')
    return render(request, 'reservas/historial_reservas.html', {'historial': historial})

@login_required
def lista_canchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'reservas/lista_canchas.html', {'canchas': canchas})

@login_required
def perfil_usuario(request):
    user = request.user
    grupos = user.groups.values_list('name', flat=True)
    rol = grupos[0] if grupos else 'Sin rol'

    return render(request, 'reservas/perfil.html', {
        'usuario': user,
        'rol': rol,
    })