from django.shortcuts import render, redirect, get_object_or_404
from ..models import Suplier, Product
from ..form import SuplierForm

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

    def filter_suplier(self, request):
        proveedores=Suplier.objects.all()
        #productos = Product.objects.all(productsuplier__suplier_id=proveedor_id)
        context = {
            'proveedores' : proveedores
        }
        return render(request, 'filter_suplier.html', context)
    
    def filter_for_suplier(self, request, suplier_id):
        productos = Product.objects.filter(productsuplier__suplier_id=suplier_id)
        context = { 
            'productos':productos
        }
        return render(request, 'filter_for_suplier.html', context)