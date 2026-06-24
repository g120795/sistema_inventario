"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import create_home,create_contact,features,category,product,stockmovement,suplier,filters

urlpatterns = [
    path('',create_home, name='home'),
    path('contact/',create_contact,name='contact'),
    path('features/', features,name='features'),
    path('features/category/',category, name='category' ),
    path('features/product/', product, name='product'),
    path('features/stockmovement/',stockmovement, name='stockmovement'),
    path('features/suplier/', suplier, name='suplier'),
    path('features/filters/', filters, name='filters'),
    path('admin/', admin.site.urls),
    path('inventory/',include('inventory.urls')),
    
]
