# ⚽ Sistema de Gestión Integral de Canchas

Este sistema permite a los usuarios gestionar reservas de canchas de fútbol de manera sencilla, ágil y clara.

---

## 🛠 Tecnologías utilizadas

- Python 3
- Django 5
- SQLite
- Bootstrap 5
- Git / GitHub

---

## ✅ Funcionalidades implementadas

- HU01: Registro de usuarios con asignación automática al grupo "cliente"
- HU08: Creación de reservas (selección de cancha, fecha y hora)
- HU09: Cancelación y modificación de reservas por el usuario
- HU11: Historial de reservas por usuario
- HU18: Visualización del estado operativo de las canchas (colores)
- Interfaz web con navegación completa (login, reservas, historial, logout)

---

## 🧑‍💻 Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/fsayago91/Ing-Software
cd sistema-canchas

2 - Crear y activar entorno virtual

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3 - Instalar Django
pip install django

4 - Instalar migraciones
python manage.py migrate

5- Crear superusuario (opcional para acceder a /admin):
python manage.py createsuperuser

6- Ejecutar el servidor
python manage.py runserver

7- Rutas principales del sistema
/registro/ → Registro de usuarios

/accounts/login/ → Inicio de sesión

/reserva/ → Formulario para crear reservas

/mis-reservas/ → Reservas activas del usuario (modificar / cancelar)

/historial/ → Historial de todas las reservas realizadas

/canchas/ → Estado operativo de todas las canchas

/admin/ → Administración Django (requiere superusuario)