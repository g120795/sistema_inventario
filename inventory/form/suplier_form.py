from django import forms
from ..models import Suplier


class SuplierForm(forms.ModelForm):
    class Meta:
        model = Suplier
        fields = [   'nombre',
                    'documento',
                    'nombre_contacto',
                    'telefono',
                    'correo',
                    'pagina_pedidos',

            ] #..