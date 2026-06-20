from django.shortcuts import render, redirect, get_object_or_404
from ..models import Category
from ..form import CategoryForm


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
        return render(request,'delete_category.html', {'category':category})#...
    

    def filter_for_category(self, request, category_id):
        producto = Product.objects.filter(categoria_id=category_id)
        return render(request, 'filter_for_category.html', {'producto':producto} )