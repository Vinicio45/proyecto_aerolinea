#django
from django import forms
# local
from .models import Pasaje

class PasajeForm(forms.ModelForm):

    class Meta:
        model = Pasaje
        fields = (
            'fecha',
            'asiento',
            'valor',
            'cliente',
            'vuelo',
        )

        widgets = {
            'fecha': forms.DateInput(
                format='%Y-%m-%d',
                attrs = {
                    'type': 'date',
                    'class': 'input-group-field',
                }
            ),
            'asiento': forms.NumberInput(
                attrs = {
                    'placeholder': 'Numero de asiento',
                    'class': 'input-group-field',
                }
            ),

            'valor': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),

        }

