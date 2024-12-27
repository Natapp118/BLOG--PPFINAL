from django.contrib import admin

from .models import Contacto, Registro, programacion,Ingenieria,formulario


# Register your models here.

admin.site.register(programacion)
admin.site.register(Ingenieria)
admin.site.register(formulario)
admin.site.register(Contacto)
admin.site.register(Registro)






