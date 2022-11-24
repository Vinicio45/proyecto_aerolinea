from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
  path(
        'persona/detalle/<pk>/', 
        views.PersonaDetailView.as_view(),
        name='detalle-persona',
    ),
]