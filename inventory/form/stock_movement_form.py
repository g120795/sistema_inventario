from django import forms
from ..models import StockMovement
from django.utils import timezone
from datetime import date


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