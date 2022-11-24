#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'panel/', 
        views.PanelHomeView.as_view(),
        name='index',
    ),

    path(
        'reporte/vuelos', 
        views.ReporteAviones.as_view(),
        name='reporte_vuelos',
    ),

    path(
        'reporte/horarios', 
        views.ReporteHorarios.as_view(),
        name='reporte_horarios',
    ),

    path(
        'reporte/pasajeros', 
        views.ReporteVuelosView.as_view(),
        name='reporte_pasajeros',
    ),

    path(
        'reporte/vuelos/print/<pk>/', 
        views.ReporteAvionesViewPdf.as_view(),
        name='vuelos_print',
    ),
   
]