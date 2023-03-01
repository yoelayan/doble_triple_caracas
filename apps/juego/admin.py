from django.contrib import admin

# Register your models here.


from .models import *
# Register your models here.

for model in [
          TipoResultado,
          Resultado
]:
     admin.site.register(model)