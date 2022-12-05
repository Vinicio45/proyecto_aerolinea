from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    FormView,
    DetailView,
    ListView,
    DeleteView,

)

from applications.persona.models import Pasaje
from .models import Cliente, Pasaje
from applications.users.mixins import AdminPermisoMixin

from applications.utils import render_to_pdf

from .forms import PasajeForm


class VuelosListView(AdminPermisoMixin, ListView):
    template_name = "vuelo/lista_vuelos.html"
    context_object_name = 'vuelos'

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        queryset = Pasaje.objects.buscar_vuelo(kword)
        return queryset

class VueloDeleteView(AdminPermisoMixin, DeleteView):
    template_name = "vuelo/eliminar_vuelo.html"
    model = Pasaje
    success_url = reverse_lazy('persona_app:lista')



class PasajeCreateView(AdminPermisoMixin, FormView):
    template_name = "vuelo/agregar_vuelo.html"
    form_class = PasajeForm
    success_url = "."

    def form_valid(self, form):

        Pasaje.objects.create(
            fecha = form.cleaned_data['fecha'],
            asiento = form.cleaned_data['asiento'],
            valor = form.cleaned_data['valor'],
            cliente = form.cleaned_data['cliente'],
            vuelo = form.cleaned_data['vuelo'],
            user=self.request.user

        )
        return super(PasajeCreateView, self).form_valid(form)



class PersonaDetailView(AdminPermisoMixin, DetailView):
    template_name = "persona/detalle_persona.html"
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        context["vuelos_mes"] = Pasaje.objects.vuelos_mes_persona(
            self.kwargs['pk']
        )
        return context