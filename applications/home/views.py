from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
)


class PanelHomeView(TemplateView):
    template_name = "home/index.html"

