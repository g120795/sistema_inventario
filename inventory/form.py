from django import forms
from .models import Product, Suplier, Category, StockMovement
from django.utils import timezone
from datetime import date


#modelo Product
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
                    'proveedores'
                   
                    
                ]

    def clean_fecha_registro(self):
        fecha = self.cleaned_data.get('fecha_registro')
        if not fecha:
            return timezone.now().date()
        return fecha #.


#modelo Suplier
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

# modelo Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['nombre']#...


#modelo StockMovement
class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = [
            'cantidad', 
            'tipo', 
            'fecha', 
            'proveedor', 
            'producto'
            ]

        
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if not fecha:
            return timezone.now().date()
        return fecha


