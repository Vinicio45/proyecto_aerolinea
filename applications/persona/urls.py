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

  path(
        'vuelo/lista_vuelos/', 
        views.VuelosListView.as_view(),
        name='lista',
    ),

   path(
        'vuelo/eliminar/<pk>/', 
        views.VueloDeleteView.as_view(),
        name='vuelo-delete',
    ),
]