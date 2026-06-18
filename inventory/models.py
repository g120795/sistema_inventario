from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        category =   (
                    f'{self.nombre}'  
        )
        return category



class Suplier(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    nombre_contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    pagina_pedidos = models.URLField(null=True, blank=True)


    def __str__(self):
        suplier =   (
                    f'{self.nombre}' 
                  
        )
        return suplier
        
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
    proveedores = models.ManyToManyField(Suplier, blank=True)

    def __str__(self):
        product = ( 
            f'{self.nombre}'  
           
        )
        return product


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
        return stock_movement





