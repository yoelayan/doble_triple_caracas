from django.shortcuts import render
from apps.juego.models import *
from apps.ventas.models import *

def get_horario(resultados):
     resultados_vesperino = resultados.filter(hora__hour__gte=12, hora__hour__lte=16)
     resultados_nocturno = resultados.filter(hora__hour__gte=19, hora__hour__lte=20)
     return resultados_vesperino, resultados_nocturno

def index(request):
     resultados_actual = Resultado.resultados_actual()
     if request.method == 'GET':
          filtro_fecha = request.GET.get('fecha')
          if filtro_fecha:
               resultados_actual = Resultado.objects.filter(fecha=filtro_fecha)
          actual_resultados_vespertino, actual_resultados_nocturno = get_horario(resultados_actual)
          return render(request, 'home/index.html', {
               'actual_resultados_vespertino': actual_resultados_vespertino,
               'actual_resultados_nocturno': actual_resultados_nocturno,
          })