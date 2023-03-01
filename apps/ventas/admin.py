from django.contrib import admin

from .models import *
# Register your models here.

for model in [
          Estado,
          Ciudad,
          TipoPersona,
          Vendedor,
          PuntoVenta
     ]:
     admin.site.register(model)