from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    DetailView
)

from applications.persona.models import Pasaje
from .models import Cliente
from applications.users.mixins import AdminPermisoMixin

from applications.utils import render_to_pdf


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