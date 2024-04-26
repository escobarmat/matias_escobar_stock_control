from django import forms

from compra.models import Producto, Proveedor


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control mb-1', 'placeholder': 'Ingrese nombre del producto...'})
        self.fields['precio'].widget.attrs.update({'class': 'form-control mb-1', 'placeholder': 'Ingrese precio del producto...'})
        self.fields['stock_actual'].widget.attrs.update({'class': 'form-control mb-1', 'placeholder': 'Ingrese stock del producto...'})
        self.fields['proveedor'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': '>>Seleccione un proveedor<<'})

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError('El precio no puede ser negativo')
        return precio

    def clean_stock_actual(self):
        stock_actual = self.cleaned_data.get('stock_actual')
        if stock_actual < 0:
            raise forms.ValidationError('El stock no puede ser negativo')
        return stock_actual

    def clean_proveedor(self):
        proveedor = self.cleaned_data.get('proveedor')
        if not proveedor:
            raise forms.ValidationError('El proveedor no puede estar vacio')
        return proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control mb-1', 'placeholder': 'Ingrese nombre del proveedor...'})
        self.fields['apellido'].widget.attrs.update({'class': 'form-control mb-1', 'placeholder': 'Ingrese apellido del proveedor...'})
        self.fields['dni'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'Ingrese DNI del proveedor...'})

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if len(apellido) < 3:
            raise forms.ValidationError('El apellido debe tener al menos 3 caracteres')
        return apellido

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if dni < 0:
            raise forms.ValidationError('El DNI no puede ser negativo')
        if len(str(dni)) < 7:
            raise forms.ValidationError('El DNI debe tener al menos 7 digitos')
        return dni