# python
from datetime import timedelta
# django
from django.utils import timezone
from django.db import models
#
from applications.vuelo.models import Avion

class PasajeManager(models.Manager):

    def resumen_vuelo_avion(self, **filters):

        if filters['date_start'] and filters['date_end'] and filters['vuelo']:
            lista_ventas = self.filter(
                #anulate=False,
                #sale__date_sale__range
                fecha__range = (
                    filters['date_start'],
                    filters['date_end'],
                ),
                #product__provider__pk=filters['provider'],
                vuelo__avion__pk=filters['vuelo'],
            ).order_by('fecha')

            return lista_ventas
        else:
            return [], 0

    
    def resumen_vuelo_hora(self, **filters):

        if filters['date_start'] and filters['date_end'] and filters['horario']:
            lista_hora = self.filter(
                #anulate=False,
                #sale__date_sale__range
                fecha__range = (
                    filters['date_start'],
                    filters['date_end'],
                ),
                #product__provider__pk=filters['provider'],
                vuelo__itinerario__hora__pk=filters['horario'],
            ).order_by('fecha')

            return lista_hora
        else:
            return [], 0