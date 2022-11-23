from django.contrib import admin

# Register your models here.
from .models import Compania, Origen, Destino, Itinerario, Vuelo, Avion, Hora

admin.site.register(Compania),
admin.site.register(Origen),
admin.site.register(Destino),
admin.site.register(Itinerario),
admin.site.register(Vuelo),
admin.site.register(Avion),
admin.site.register(Hora),