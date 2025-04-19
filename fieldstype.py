from django.db import models
import uuid


# Modelo de ejemplo que incluye todos los tipos de campos principales
class EjemploModelo(models.Model):
    # --- Campos básicos ---
    campo_texto = models.CharField(max_length=100)  # Texto corto (ej: "Hola Mundo")
    campo_texto_largo = models.TextField()  # Texto largo (ej: "Lorem ipsum...")
    campo_entero = models.IntegerField()  # Entero (ej: 42)
    campo_entero_grande = models.BigIntegerField()  # Entero grande (ej: 9223372036854775807)
    campo_decimal = models.DecimalField(max_digits=5, decimal_places=2)  # Decimal (ej: 19.99)
    campo_booleano = models.BooleanField(default=False)  # True/False (ej: True)

    # --- Fechas y horas ---
    fecha = models.DateField()  # Fecha (ej: "2023-12-31")
    fecha_hora = models.DateTimeField()  # Fecha y hora (ej: "2023-12-31 23:59:59")
    hora = models.TimeField()  # Hora (ej: "23:59:59")

    # --- Campos especializados ---
    email = models.EmailField()  # Email válido (ej: "user@example.com")
    url = models.URLField()  # URL válida (ej: "https://example.com")
    uuid = models.UUIDField(default=uuid.uuid4)  # Identificador único (ej: "a1b2c3d4-...")
    json = models.JSONField()  # Datos JSON (ej: {"key": "value"})

    # --- Archivos e imágenes ---
    archivo = models.FileField(upload_to='archivos/')  # Subir archivo (ej: "archivos/doc.pdf")
    imagen = models.ImageField(upload_to='imagenes/')  # Subir imagen (requiere Pillow)

    # --- Relaciones ---
    # ForeignKey (muchos a uno)
    # ManyToManyField (muchos a muchos)
    # OneToOneField (uno a uno)
    # Nota: Estas relaciones necesitan modelos adicionales para funcionar

    # --- Campos automáticos ---
    creado = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    actualizado = models.DateTimeField(auto_now=True)  # Fecha de actualización automática

    def __str__(self):
        return self.campo_texto


# Modelos adicionales para demostrar relaciones
class Autor(models.Model):
    nombre = models.CharField(max_length=100)


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  # Muchos libros pueden tener un autor


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)


class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    etiquetas = models.ManyToManyField(Etiqueta)  # Un artículo puede tener muchas etiquetas


class Perfil(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # 1:1 con User
    bio = models.TextField()

# Notas importantes:
# 1. Para ImageField necesitas instalar Pillow: pip install pillow
# 2. Algunos campos como JSONField funcionan mejor con PostgreSQL
# 3. Las relaciones (ForeignKey, etc.) requieren modelos relacionados
# 4. auto_now_add establece la fecha solo al crear, auto_now actualiza cada vez que se guarda