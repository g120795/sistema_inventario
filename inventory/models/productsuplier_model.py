from django.db import models
from .product_model import Product
from .suplier_model import Suplier


class ProductSuplier(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    suplier = models.ForeignKey(Suplier, on_delete=models.CASCADE)
