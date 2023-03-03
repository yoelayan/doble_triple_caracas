from django.shortcuts import render
from apps.juego.models import *
from apps.ventas.models import *

def get_horario(resultados):
     resultados_vesperino = resultados.filter(hora__hour__gte=12, hora__hour__lte=16)
     resultados_nocturno = resultados.filter(hora__hour__gte=19, hora__hour__lte=20)
     return resultados_vesperino, resultados_nocturno

def index(request):
     from django.core.paginator import Paginator
     resultados_actual = Resultado.resultados_actual()
     
     if request.method == 'GET':
          
          ciudad = request.GET.get('ciudad')
          page_number = request.GET.get('page')
          filtro_fecha = request.GET.get('fecha')
          
          puntos_venta = PuntoVenta.objects.all()
          if ciudad:
               puntos_venta = puntos_venta.filter(ciudad=ciudad)
          puntos_venta = Paginator(puntos_venta, 5)
          puntos_venta = puntos_venta.get_page(page_number)
          
          if filtro_fecha:
               resultados_actual = Resultado.objects.filter(fecha=filtro_fecha)   
          actual_resultados_vespertino, actual_resultados_nocturno = get_horario(resultados_actual)
          
          return render(request, 'home/index.html', {
               'actual_resultados_vespertino': actual_resultados_vespertino,
               'actual_resultados_nocturno': actual_resultados_nocturno,
               'puntos_venta': puntos_venta,
               'ciudades': Ciudad.objects.all()
          })