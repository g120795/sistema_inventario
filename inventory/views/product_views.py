from django.shortcuts import render, redirect, get_object_or_404
from ..models import Product
from ..form import ProductForm
# vista producto
class CRUDProduct:
    def list_inventory(self,request):
        lista_inventario = 'lista_inventario'
        return render(request, 'inventory.html', {'lista_inventario':lista_inventario})
    #crear producto
    def create_product(self,request):
        if request.method == 'POST':
            print("post verificado")
            form = ProductForm(request.POST)
            print(form.errors)
            if form.is_valid():
                print("DATOS DEL FORMULARIO VALIDOS")
                form.save()
                print("datos guardados en la db")
                return redirect('read_inventory')
            else:
                print("no valido")
        else:
            print("en el formulario")
            form = ProductForm()
        return render(request,'create_product.html',{'form':form})
        pass

    #leer inventario
    def read_inventory(self,request):
        print(request.method)
        products = Product.objects.all()
        return render(request,'read_inventory.html', {'product':products})
    
    #actualizar producto
    def update_product(self,request,producto_id):
        product = get_object_or_404(Product, id=producto_id)
        if request.method == 'POST':
            print("post verificado")
            form = ProductForm(request.POST,instance=product)
            print(form.errors)
            if form.is_valid():
                print("DATOS DEL FORMULARIO VALIDOS")
                form.save()
                print("datos guardados en la db")
                return redirect('read_inventory')
            else:
                print("no valido")
        else:
            print("en el formulario")
            form = ProductForm(instance=product)
        return render(request,'update_product.html',{'form':form})
        
    #eliminar producto
    def delete_product(self,request,producto_id):
        producto = get_object_or_404(Product, id=producto_id)
        if request.method == 'POST':
            producto.delete()
            return redirect('read_inventory')
        return render(request,'delete_product.html',{'producto':producto}) #.
