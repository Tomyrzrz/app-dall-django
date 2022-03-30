from django.db import models
import datetime 

# Create your models here.
class Producto(models.Model):
  nombre = models.CharField(max_length=100, blank=False, null=False)
  descripcion = models.TextField(blank=False, null=False)
  costo = models.FloatField(blank=False, null=False)
  descripcion_corta = models.CharField(max_length=100, blank=False, null=False)
  imagen = models.ImageField(null=True, upload_to='productos')
  fecha_creacion = models.DateField(default=datetime.date.today, blank=False, null=False)#DateTimeField
  disponible = models.BooleanField(default=True)
  cantidad = models.IntegerField(null=False, default=100)
  enlace = models.URLField() 

  def __str__(self):
    return self.nombre
  
  class Meta:
    verbose_name = ("Product")
    verbose_name_plural = ("Products Dell")

class Servicio(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.TextField()
  costo = models.FloatField(null=False, default=0.0)
  fecha_creacion = models.DateTimeField(null=False, default=datetime.datetime.now)

  def __str__(self):
    return self.nombre
  class Meta:
    verbose_name = ("Service")
    verbose_name_plural = ("Services Dell")

class Comentarios(models.Model):
  nombre = models.CharField(max_length=150, blank=False, null=False)
  email = models.EmailField(max_length=150, blank=False, null=False)
  website = models.URLField(max_length=120, blank=False, null=False)
  comentario = models.TextField(blank=False, null=False)
  fecha_creacion = models.DateTimeField(default=datetime.date.today, blank=False, null=False)#DateTimeField

  class Meta:
    verbose_name = ("Comment")
    verbose_name_plural = ("Comments")
  
  def __str__(self):
    return self.nombre




# TAREA
# Identificar producto o servicio de tu tema
# definen que atributos tiene ese producto o servicio

# python manage.py makemigrations    para crear el archivo de migracion
# python manage.py migrate           para hacer la migracion a la BD
# python manage.py runserver         Para correr la app
# python manage.py createsuperuser   Para crear el super usuario de Admin
