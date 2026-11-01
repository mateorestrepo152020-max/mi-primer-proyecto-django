# Mi Primer Proyecto Django

Ejercicio práctico del curso de Django.

## Descripción

Proyecto básico de Django con una app llamada **saludos** que muestra mensajes de bienvenida y despedida.

## Estructura del proyecto

```
mi_primer_proyecto/
├── manage.py
├── mi_primer_proyecto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── saludos/
    ├── __init__.py
    ├── apps.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── models.py
    └── tests.py
```

## Cómo ejecutarlo

1. Activa tu entorno virtual (si tienes uno):
   ```bash
   source venv/bin/activate   # Linux/Mac
   # o
   venv\Scripts\activate      # Windows
   ```

2. Instala Django (si no lo tienes):
   ```bash
   pip install django
   ```

3. Entra a la carpeta del proyecto:
   ```bash
   cd mi_primer_proyecto
   ```

4. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

5. Abre tu navegador en:
   - **http://127.0.0.1:8000/saludos/** → Mensaje de bienvenida
   - **http://127.0.0.1:8000/saludos/adios/** → Mensaje de despedida (reto adicional)

## Vistas implementadas

| Ruta              | Descripción                          |
|-------------------|--------------------------------------|
| `/saludos/`       | "Bienvenido al curso de Django, Mateo Restrepo" |
| `/saludos/adios/` | Mensaje de despedida (reto opcional) |

## Notas

- La app `saludos` está registrada en `INSTALLED_APPS`.
- Las URLs de la app están incluidas en el `urls.py` del proyecto.
- Se incluye el reto adicional de la vista de despedida.
