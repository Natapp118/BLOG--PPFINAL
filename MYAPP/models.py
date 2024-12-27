from django.db import models

# Create your models here.
class programacion(models.Model):
    nombre = models.CharField(max_length=40)
    ID = models.IntegerField() 
    email = models.EmailField()

    
    def __str__(self):
        return f"Nombre del proyecto: {self.nombre}"


class Ingenieria(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
def __str__(self):
        return f"Nombre de Proyecto {self.nombre}"

class formulario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
def __str__(self):
        return f"Nombre : {self.nombre}"


class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    Mensaje = models.EmailField()
def __str__(self):
        return f"Nombre de Proyecto {self.nombre}"


class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    Mensaje = models.EmailField()
def __str__(self):
        return f"Registro {self.nombre}"

class login_view(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
def __str__(self):
        return f"Nombre de Proyecto {self.nombre}"
