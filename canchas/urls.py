from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservas.urls')),  # URLs propias de tu app
    path('accounts/', include('django.contrib.auth.urls')),  # 👈 Agregar esta línea
]
