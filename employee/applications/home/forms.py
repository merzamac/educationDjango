from django import forms
from .models import Prueba


class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        #fields = ("__all__")
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo':forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese aqui',
                    'class':'type1'

                }
            )
        }
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('debe ser mayor que 10')

        return cantidad