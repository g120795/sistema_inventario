from django.urls import path
from .views import CRUDProduct, CRUDSuplier, CRUDCategory, CRUDStockMovement

views_product = CRUDProduct()
views_suplier = CRUDSuplier()
views_category = CRUDCategory()
views_stock_movement = CRUDStockMovement()
urlpatterns = [ 

    #urls product
   
    path('create_product/', views_product.create_product, name='create_product'),
    path('read_inventory/', views_product.read_inventory, name='read_inventory'),
    path('<int:producto_id>/edit_product/', views_product.update_product, name='update_product'),
    path('<int:producto_id>/delete_product/', views_product.delete_product, name='delete_product'),
    

    #urls suplier
    path('create_suplier/', views_suplier.create_suplier, name='create_suplier'),
    path('read_suplier/', views_suplier.read_suplier, name='read_suplier'),
    path('<int:suplier_id>/update_suplier/',views_suplier.update_suplier, name='update_suplier'),
    path('<int:suplier_id>/delete_suplier/', views_suplier.delete_suplier, name='delete_suplier'),
    path('<int:proveedor_id>/filter_for_suplier/', views_suplier.filter_for_suplier,name='filter_for_suplier'),

    #urls category
    path('create_category/', views_category.create_category, name='create_category'),
    path('read_category/', views_category.read_category, name='read_category'),
    path('<int:category_id>/update_category/', views_category.update_category, name='update_category'),
    path('<int:category_id>/delete_category/', views_category.delete_category, name='delete_category'),
    path('<int:category_id>/filter_for_category/', views_category.filter_for_category, name='filter_for_category'),
    
    #urls stock_movement
    path('create_stock_movement/', views_stock_movement.create_stock_movement, name='create_stock_movement'),
    path('read_stock_movement/', views_stock_movement.read_stock_movement, name='read_stock_movement')

]