from django.shortcuts import render, redirect, get_object_or_404
from .form import ProductForm, SuplierForm, CategoryForm
from .models import Product, Suplier, Category


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
                return redirect('list_inventory')
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


#clase proveedores
class CRUDSuplier:
    def create_suplier(self, request):
        if request.method == 'POST':
            form = SuplierForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('read_suplier')
        else:
            form = SuplierForm()
        return render(request, 'create_suplier.html', {'form': form})
    

    def read_suplier(self, request):
        suplier = Suplier.objects.all()
        return render(request, 'read_suplier.html',{'suplier':suplier})
    

    def update_suplier(self, request, suplier_id):
        suplier = get_object_or_404(Suplier, id=suplier_id)
        if request.method == 'POST':
            form = SuplierForm(request.POST, instance=suplier)
            if form.is_valid():
                form.save()
                return redirect('read_suplier')
        else:
            form = SuplierForm(instance=suplier)
        return render(request, 'update_suplier.html', {'form':form})


    def delete_suplier(self, request, suplier_id):
        suplier = get_object_or_404(Suplier, id=suplier_id)
        if request.method == 'POST':
            suplier.delete()
            return redirect('read_suplier')
        return render(request,'delete_suplier.html', {'suplier':suplier}) #..



class CRUDCategory:
    def create_category(self, request):
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('read_category')
        else:
            form = CategoryForm()
        return render(request,'create_category.html',{'form':form})
    
    def read_category(self, request):
        categorys = Category.objects.all()
        return render(request,'read_category.html', {'categorys':categorys})

    def update_category(self, request, category_id):
        categorys= get_object_or_404(Category, id=category_id)
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=categorys)
            if form.is_valid():
                form.save()
                return redirect('read_category')
        else:
            form = CategoryForm(instance=categorys)
        return render(request, 'update_category.html', {'form':form})

    def delete_category(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        if request.method == 'POST':
            category.delete()
            return redirect('read_category')
        return render(request,'delete_category.html', {'category':category})














































