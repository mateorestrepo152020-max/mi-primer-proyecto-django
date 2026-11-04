from django.http import HttpResponse
from .models import Libro


def resumen(request):
    total = Libro.objects.count()
    return HttpResponse(
        f"Actualmente hay {total} libros registrados en la biblioteca."
    )
from rest_framework import viewsets
from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('titulo')
    serializer_class = LibroSerializer