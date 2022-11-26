from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    FormView,
    DetailView,

)

from applications.persona.models import Pasaje
from .models import Cliente
from applications.users.mixins import AdminPermisoMixin

from applications.utils import render_to_pdf

from .forms import PasajeForm


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