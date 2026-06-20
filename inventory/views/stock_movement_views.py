from django.shortcuts import render, redirect, get_object_or_404
from ..models import StockMovement
from ..form import StockMovementForm, Product


class CRUDStockMovement:
    alerta_stock_minimo = False


    def update_product(self,request):
        nombres = ['cantidad', 'tipo', 'proveedor', 'producto']
        producto = {nombre:valor for nombre, valor in request.POST.items() if nombre in nombres}
        print(producto)
        product = Product.objects.get(id=producto['producto'])
        print(product.stock_actual)
        print(product.stock_minimo)
        if producto['tipo'] == 'entrada':
            product.stock_actual += int(producto['cantidad'])

        elif producto['tipo'] == 'salida':
            product.stock_actual -=  int(producto['cantidad'])
        
        if product.stock_actual <= product.stock_minimo:
            self.alerta_stock_minimo = True
        return product


    def create_stock_movement(self, request):
        self.alerta_stock_minimo = False
        if request.method == 'POST':
            form = StockMovementForm(request.POST)
            if form.is_valid():
                form.save()
                self.update_product(request).save()
                if self.alerta_stock_minimo == True:
                    return redirect('read_inventory')
                return redirect('read_stock_movement')
        else:
            form = StockMovementForm()
        print(form)        
        return render(request, 'create_stock_movement.html', {'form':form})
           

    def read_stock_movement(self, request):
        stock_movement = StockMovement.objects.all()
        return render(request, 'read_stock_movement.html', {'stock_movement':stock_movement})
