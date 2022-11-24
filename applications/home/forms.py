from django import forms

from applications.vuelo.models import Avion, Hora, Vuelo

class VuelosAvionForm(forms.Form):

    vuelo = forms.ModelChoiceField(
        required=True,
        queryset=Avion.objects.all(),
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',
            }
        )
    )
    date_start = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )
    date_end = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )


class VuelosHorarioForm(forms.Form):

    horario = forms.ModelChoiceField(
        required=True,
        queryset=Hora.objects.all(),
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',
            }
        )
    )
    date_start = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )
    date_end = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )

class VuelosPasajerosForm(forms.Form):

    vuelo = forms.ModelChoiceField(
        required=True,
        queryset=Vuelo.objects.all(),
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',
            }
        )
    )
    date_start = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )
