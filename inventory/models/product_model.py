from django.db import models
from .category_model import Category
from .suplier_model import Suplier

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    serie = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_registro = models.DateField(blank=True)
    stock_actual = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField()
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE) # EN ESTE CASO SI ELIMINO UNA CATEGORIA, TODOS LOS PRODUCTOS ASOCIADAS A ESA CATEGORIA TAMBIEN SE ELIMINARAN
    proveedores = models.ManyToManyField(Suplier, blank=True, through='ProductSuplier')

    def __str__(self):
        product = ( 
            f'{self.nombre}'  
           
        )
        return product #...