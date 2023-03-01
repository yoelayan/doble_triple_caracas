from django.db import models
from apps.core.models import CommonModel
# Create your models here.


class Estado(CommonModel):
     pass

class Ciudad(CommonModel):
     estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
     pass

class TipoPersona(CommonModel):
     pass

class Vendedor(models.Model):
     TIPO_DOCUMENTO = (
          ('J', 'JURIDICO'),
          ('N', 'NATURAL'),
     )
     tipo_persona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)
     tipo_documento = models.CharField(max_length=1, choices=TIPO_DOCUMENTO)
     numero_documento = models.CharField( max_length=50)
     nombre = models.CharField(max_length=250)
     estado = models.ForeignKey(Estado, related_name='vendedores', on_delete=models.DO_NOTHING)
     ciudad = models.ForeignKey(Ciudad, related_name='vendedores', on_delete=models.DO_NOTHING)
     direccion = models.TextField()
     correo = models.CharField(max_length=150)
     telefono = models.CharField(max_length=50)
     
class PuntoVenta(CommonModel):
     ciudad = models.ForeignKey(Ciudad, related_name='ciudades', on_delete=models.CASCADE)
     direccion = models.TextField()
     vendedor = models.ForeignKey(Vendedor, related_name='puntos_de_venta', on_delete=models.CASCADE)


