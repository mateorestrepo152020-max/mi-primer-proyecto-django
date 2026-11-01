from django.http import HttpResponse


def saludo(request):
    """Vista principal que muestra el mensaje de bienvenida."""
    return HttpResponse("Bienvenido al curso de Django, Mateo Restrepo")


def adios(request):
    """Vista adicional (reto opcional) con mensaje de despedida."""
    return HttpResponse("¡Hasta luego! Gracias por aprender Django. ¡Éxito!")
