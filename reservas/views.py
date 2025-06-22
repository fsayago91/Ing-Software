from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReservaForm

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