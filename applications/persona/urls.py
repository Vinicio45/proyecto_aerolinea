from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
  path(
        'vuelo/crear_pasaje/', 
        views.PasajeCreateView.as_view(),
        name='persona_add',
    ),

  path(
        'persona/detalle/<pk>/', 
        views.PersonaDetailView.as_view(),
        name='detalle',
    ),
]