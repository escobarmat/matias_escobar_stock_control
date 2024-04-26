from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from compra.forms import ProductoForm, ProveedorForm
from compra.models import Producto, Proveedor


# Create your views here.

def home(request):
    return redirect('compra:productos')
def productos(request):
    productos = Producto.objects.all()
    paginacion = Paginator(productos, 7)
    page_number = request.GET.get("page")
    page_obj = paginacion.get_page(page_number)
    return render(request, 'compra/index.html', {'page_obj': page_obj})


def proveedores(request):
    proveedores = Proveedor.objects.all()
    paginacion = Paginator(proveedores, 7)
    page_number = request.GET.get("page")
    page_obj = paginacion.get_page(page_number)
    return render(request, 'compra/proveedores.html', {'page_obj': page_obj})


def alta_proveedor(request):
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            nuevo_proveedor = proveedor_form.save(commit=True)
            messages.success(request, 'Proveedor creado con exito')
            return redirect(reverse('compra:proveedores'))
    else:
        proveedor_form = ProveedorForm()
    return render(request, 'compra/alta_proveedor.html', {'form': proveedor_form})


def alta_producto(request):
    nuevo_producto = None
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            nuevo_producto = producto_form.save(commit=True)
            messages.success(request, 'Producto creado con exito')
            return redirect(reverse('compra:productos'))
    else:
        producto_form = ProductoForm()
    return render(request, 'compra/alta_producto.html', {'form': producto_form})
