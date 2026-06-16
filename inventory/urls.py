from django.urls import path
from .views import CRUDProduct

views_product=CRUDProduct()
urlpatterns = [ 
    path('inventory/',views_product.list_inventory,name='list_inventory'),
    path('create_product/',views_product.create_product,name='create_product')
    
]