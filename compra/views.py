from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect

from compra.models import Producto, Proveedor


# Create your views here.

def productos(request):
    productos = Producto.objects.all()
    messages = get_messages(request)
    return render(request, 'compra/index.html', {'productos': productos, 'messages': messages})

def proveedores(request):
    proveedores = Proveedor.objects.all()
    messages = get_messages(request)
    return render(request, 'compra/proveedores.html', {'proveedores': proveedores, 'messages': messages})
def alta_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        proveedor = Proveedor.objects.create(
            nombre=nombre,
            apellido=apellido,
            dni=dni
        )
        proveedor.save()
        messages.success(request, 'Proveedor creado con exito')
        return redirect('compra:proveedores')

    return render(request, 'compra/alta_proveedor.html')

def alta_producto(request):
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        proveedor_id = request.POST.get('proveedor_id')
        proveedor = Proveedor.objects.get(id=proveedor_id)
        producto = Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock_actual=stock_actual,
            proveedor=proveedor
        )
        producto.save()
        messages.success(request, 'Producto creado con exito')
        return redirect('compra:productos')
    return render(request, 'compra/alta_producto.html', {'proveedores': proveedores})