from django.db import models

# Create your models here.

class Category(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        category =   (
                    f'{self.nombre}'  
        )
        return category #.