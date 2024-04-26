from django.urls import path, re_path
from .views import *

app_name = 'compra'

urlpatterns = [
    path('', productos, name='productos'),
    path('proveedores/', proveedores, name='proveedores'),
    path('alta_proveedor/', alta_proveedor, name='alta_proveedor'),
    path('alta_producto/', alta_producto, name='alta_producto'),
    re_path(r'^.*$', home, name='home'),
 ]
