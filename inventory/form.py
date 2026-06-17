from django import forms
from .models import Product, Suplier, Category
from django.utils import timezone
from datetime import date

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [  'nombre',
                    'modelo',
                    'serie',
                    'color',
                    'precio',
                    'fecha_vencimiento',
                    'fecha_registro',
                    'stock_actual',
                    'stock_minimo',
                    'categoria',
                    
                ]
    def clean_fecha_registro(self):
        fecha = self.cleaned_data.get('fecha_registro')
        if not fecha:
            return timezone.now().date()
        return fecha #.


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


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['nombre']



