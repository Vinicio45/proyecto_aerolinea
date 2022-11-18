from model_utils.models import TimeStampedModel

from django.db import models

# Create your models here.

class Compania(TimeStampedModel):

    name = models.CharField(
        'Nombre del avion', 
        max_length=100
    )

    class Meta:
        verbose_name = 'Compañia'
        verbose_name_plural = 'Compañias'

    def __str__(self):
        return self.name



class Origen(TimeStampedModel):

    ciudad = models.CharField(
        'nombre de la ciudad', 
        max_length=40
    )

    pais = models.CharField(
        'nombre del pais', 
        max_length=40
    )

    class Meta:
        verbose_name = 'Origen vuelo'

    def __str__(self):
        return self.ciudad



class Destino(TimeStampedModel):

    ciudad = models.CharField(
        'nombre de la ciudad', 
        max_length=40
    )

    pais = models.CharField(
        'nombre del pais', 
        max_length=40
    )

    class Meta:
        verbose_name = 'Destino'
        verbose_name_plural = 'Destino'

    def __str__(self):
        return self.name


class Itinerario(TimeStampedModel):

    fecha = models.DateField(
        'fecha del vuelo',
        blank=True, 
        null=True
    )

    origen = models.ForeignKey(
        Origen, 
        on_delete=models.CASCADE
    )

    destino = models.ForeignKey(
        Destino, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Itinerario'
        verbose_name_plural = 'Itinerarios'

    def __str__(self):
        return self.origen +" - "+self.destino

class Vuelo(TimeStampedModel):

    capacidad = models.PositiveIntegerField(
        'capacidad del avion',
        default=0
    )

    modelo_avion = models.CharField(
        'modelo del avion', 
        max_length=20
    )

    compania = models.ForeignKey(
        Compania, 
        on_delete=models.CASCADE
    )

    itinerario = models.ForeignKey(
        Itinerario, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Vuelo'
        verbose_name_plural = 'Vuelos'

    def __str__(self):
        return self.modelo_avion