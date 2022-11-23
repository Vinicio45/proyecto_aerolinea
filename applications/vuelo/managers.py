# python
from datetime import timedelta
# django
from django.utils import timezone
from django.db import models
#
from applications.vuelo.models import Vuelo

class PasajeManager(models.Manager):

    def resumen_vuelo_avion(self, **filters):

        if filters['date_start'] and filters['date_end'] and filters['vuelo']:
            consulta = self.filter(
                pasaje__fecha__range = (
                    filters['date_start'],
                    filters['date_end'],
                ),
                vuelo__icontains = 'vuelo',
            )
            return consulta
        else:
            return [], 0