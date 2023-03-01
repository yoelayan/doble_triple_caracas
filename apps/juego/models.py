# Django Modules
from django.db import models

# Local Modules
from apps.core.models import CommonModel

class TipoResultado(CommonModel):
     pass

class Resultado(models.Model):
     tipo = models.ForeignKey(TipoResultado, related_name="resultados", on_delete=models.CASCADE)
     fecha = models.DateField(auto_now=False, auto_now_add=False)
     hora = models.TimeField(auto_now=False, auto_now_add=False)
     concepto_1 = models.CharField(max_length=255)
     concepto_2 = models.CharField(max_length=255)
     
     def __str__(self):
          return self.tipo.description
     
     @staticmethod
     def resultados_actual():
          from datetime import datetime
          return Resultado.objects.filter(
               fecha=datetime.now()
          )
          