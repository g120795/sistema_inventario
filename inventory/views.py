from django.shortcuts import render,redirect
from .form import ProductForm
# Create your views here.
class CRUDProduct():
    def list_inventory(self,request):
        lista_inventario = 'lista_inventario'
        return render(request, 'inventory.html', {'lista_inventario':lista_inventario})

    def create_product(self,request):
        if request.method == 'POST':
            print("post verificado")
            form = ProductForm(request.POST)
            print(form.errors)
            if form.is_valid():
                print("DATOS DEL FORMULARIO VALIDOS")
                form.save()
                
                print("datos guardados en la db")
                redirect('list_inventory')
            else:
                print("no valido")
        else:
            print("en el formulario")
            form = ProductForm()
        return render(request,'in_product.html',{'form':form})
        pass

    def read_inventory(self,request):
        pass

    def update_inventory(self,request):
        pass

    def delete_items(self,request):
        pass