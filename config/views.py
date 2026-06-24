from django.shortcuts import render, redirect, get_object_or_404

def create_home(request):
    return render(request, 'home.html')

def create_contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

###


def category(request):
    return render(request, 'category.html')

def product(request):
    return render(request, 'product.html')

def stockmovement(request):
    return render(request, 'stockmovement.html')

def suplier(request):
    return render(request, 'suplier.html')







"""<li><a href="{% url 'update_product' product_id%}">actualizar producto</li>
    <br>    
<li><a href="{% url 'delete_product' product_id %}">eliminar producto</li>
    <br>
 <li><a href="{% url 'update_suplier' suplier_id %}">actualizar proveedor</li>
    <br>
    <li><a href="{% url 'delete_suplier' suplier_id%}">eliminar proveedor</li>
    <br>
    <li><a href="{% url 'filter_for_suplier' proveedor_id%}">filtrar por proveedor</li>
    <br>
    <li><a href="{% url 'update_category' category_id%}">actualizar categoria</li>
    <br>
    <li><a href="{% url 'delete_category' category_id%}">eliminar categoria</li>
    <br>
    <li><a href="{% url 'filter_for_category' category_id%}">filtrar por categoria</li>
    <br>

"""