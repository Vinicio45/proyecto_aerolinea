from django.contrib import admin

# Register your models here.

from .models import Cliente, Pasaje

admin.site.register(Cliente),
admin.site.register(Pasaje),