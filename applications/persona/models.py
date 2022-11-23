from model_utils.models import TimeStampedModel
from django.conf import settings

from django.db import models

from applications.vuelo.models import Vuelo

from .managers import PasajeManager
# Create your models here.




class Cliente(TimeStampedModel):

    nombres = models.CharField(
        'Nombres', 
        max_length=30
    )

    apellidos = models.CharField(
        'Apellidos', 
        max_length=30
    )

    edad = models.PositiveIntegerField(
        'Edad',
        default=0
    )

    telefono = models.CharField(
        'Telefono',
        max_length=40,
        blank=True,
    )

    Nacionalidad = models.CharField(
        'Nacionalidad', 
        max_length=100
    )

    def __str__(self):
        return self.nombres + ' ' + self.apellidos




class Pasaje(TimeStampedModel):

    fecha = models.DateField(
        'fecha del vuelo',
        blank=True, 
        null=True
    )

    asiento = models.PositiveIntegerField(
        'numero de asiento',
        default=0
    )

    valor = models.DecimalField(
        'valor del boleto', 
        max_digits=10, 
        decimal_places=2
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='cajero',
        related_name="user_venta",
    )

    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE
    )

    vuelo = models.ForeignKey(
        Vuelo, 
        on_delete=models.CASCADE
    )

    objects = PasajeManager()

    def __str__(self):
        return str(self.cliente) + ' - ' + str(self.vuelo)
