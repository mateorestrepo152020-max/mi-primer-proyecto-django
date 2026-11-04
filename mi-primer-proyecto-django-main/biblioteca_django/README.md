# Biblioteca — Proyecto Django (Sesión 4 — Ejercicio integrador)

Proyecto completo que integra: Introducción a Django, Modelos/ORM y Django Admin.

## Estructura

```
biblioteca_django/
├── manage.py
├── config/           # Proyecto
│   ├── settings.py   # biblioteca en INSTALLED_APPS
│   └── urls.py       # include de biblioteca.urls
└── biblioteca/       # App
    ├── models.py     # Autor + Libro (ForeignKey)
    ├── admin.py      # list_display, list_filter, search_fields
    ├── views.py      # vista resumen
    └── urls.py       # /biblioteca/resumen/
```

## Cómo ejecutarlo

```bash
# (opcional) entorno virtual
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install django

cd biblioteca_django
python manage.py migrate
python manage.py createsuperuser   # o usa admin / admin123 si ya existe
python manage.py runserver
```

### Cargar datos de prueba (si la base está vacía)

```bash
python manage.py shell
```

```python
from biblioteca.models import Autor, Libro
a1 = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombia")
a2 = Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chile")
Libro.objects.create(titulo="Cien años de soledad", autor=a1, precio=68000)
Libro.objects.create(titulo="El amor en los tiempos del cólera", autor=a1, precio=55000)
Libro.objects.create(titulo="La casa de los espíritus", autor=a2, precio=60000)
```

## URLs

| Ruta | Descripción |
|------|-------------|
| http://127.0.0.1:8000/admin/ | Panel de administración |
| http://127.0.0.1:8000/biblioteca/resumen/ | Cuenta de libros registrados |

### Superusuario de prueba (si se creó en este entorno)

- Usuario: `admin`
- Contraseña: `admin123`

## Checklist del ejercicio

- [x] Proyecto `config` y app `biblioteca`
- [x] App registrada en `INSTALLED_APPS`
- [x] Modelos `Autor` y `Libro` con `ForeignKey` + `on_delete` + `__str__`
- [x] Migraciones
- [x] Admin con `list_display`, `list_filter`, `search_fields`
- [x] Vista `resumen` en `/biblioteca/resumen/`
