"""
URL configuration for mi_primer_proyecto project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludos/', include('saludos.urls')),  # Conectamos la app saludos
]
