from django.db import models
from .product_model import Product
from .suplier_model import Suplier

class StockMovement(models.Model):
    TIPO_CHOICES = [ 
    ('entrada','Entrada'),
    ('salida','Salida')
    ]
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha = models.DateField(blank=True)
    proveedor = models.ForeignKey(Suplier, null=True, blank=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        stock_movement =   (
                    f'{self.cantidad}' 
                    f'{self.tipo}' 
                    f'{self.fecha}'
                    f'{self.proveedor}' 
                    f'{self.producto}' 
        )
        return stock_movement #....