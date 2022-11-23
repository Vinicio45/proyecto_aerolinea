from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    ListView,
    View
)

from applications.persona.models import Pasaje
from applications.users.mixins import AdminPermisoMixin
from .forms import VuelosAvionForm, VuelosHorarioForm

from applications.utils import render_to_pdf

class PanelHomeView(TemplateView):
    template_name = "home/index.html"


class ReporteAviones(AdminPermisoMixin, ListView):
    template_name = "home/reporte_vuelos.html"
    context_object_name = "vuelos_avion"
    extra_context = {'form': VuelosAvionForm}
    
    def get_queryset(self):   

        lista_ventas = Pasaje.objects.resumen_vuelo_avion(
            vuelo=self.request.GET.get("vuelo", ''),
            date_start=self.request.GET.get("date_start", ''),
            date_end=self.request.GET.get("date_end", ''),
        )
        return lista_ventas

class ReporteAvionesViewPdf(AdminPermisoMixin, View):
    
    def get(self, request, *args, **kwargs):
        lista_ventas = Pasaje.objects.resumen_vuelo_avion(
            vuelo=self.request.GET.get("vuelo", ''),
            date_start=self.request.GET.get("date_start", ''),
            date_end=self.request.GET.get("date_end", ''),
        )
        data = {
            'lista_venta': lista_ventas,
        }
        pdf = render_to_pdf('producto/detail-print.html', data)
        return HttpResponse(pdf, content_type='application/pdf')



class ReporteHorarios(AdminPermisoMixin, ListView):
    template_name = "home/reporte_horarios.html"
    context_object_name = "vuelos_hora"
    extra_context = {'form': VuelosHorarioForm}
    
    def get_queryset(self):   

        lista_hora = Pasaje.objects.resumen_vuelo_avion(
            vuelo=self.request.GET.get("horario", ''),
            date_start=self.request.GET.get("date_start", ''),
            date_end=self.request.GET.get("date_end", ''),
        )
        return lista_hora

