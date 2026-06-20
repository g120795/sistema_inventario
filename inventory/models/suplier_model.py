from django.db import models

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
        return suplier #..