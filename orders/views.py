from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .carro import Carro
from products.models import Producto, AtributoProducto
# Create your views here.

def agregar_producto(request, producto_id, atributo_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    atributo = AtributoProducto.objects.get(id=atributo_id)
    carro.agregar(producto, atributo)
    
    return redirect('carro:ver_carrito')

@require_POST
def eliminar_producto(request, producto_id, atributo_id):
    carro = Carro(request)
    carro.eliminar(producto_id, atributo_id)
    return redirect('carro:ver_carrito')



def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect('carro:ver_carrito')

def limpiar_carro(request):
    request.session['carro'] = {}
    request.session.modified = True
    return redirect('carro:ver_carrito')


def agregar_desde_formulario(request, producto_id):
    atributo_id = request.POST.get('atributo_id')
    cantidad = int(request.POST.get('cantidad', 1))
    if atributo_id:
        return redirect('carro:agregar', producto_id=producto_id, atributo_id=atributo_id)
    else:
        messages.error(request, "Debes seleccionar una talla.")
        return redirect('products:producto_detail', producto_id=producto_id)


def ver_carrito(request):
    carro = request.session.get('carro', {})
    items = []

    for clave, datos in carro.items():
        if 'atributo_id' not in datos:
            continue  # omite entradas corruptas

        producto = Producto.objects.get(id=datos['producto_id'])
        atributo = AtributoProducto.objects.get(id=datos['atributo_id'])
        subtotal = producto.precio * datos['cantidad']
        items.append({
            'producto': producto,
            'atributo': atributo,
            'cantidad': datos['cantidad'],
            'subtotal': subtotal,
        })

    total = sum(item['subtotal'] for item in items)
    print("Carrito leído:", carro)
    print("Items reconstruidos:", items)
    return render(request, 'carrito/ver_carrito.html', {'items': items, 'total': total})


@login_required
def finalizar_compra(request):
    carro = Carro(request)
    pedido = carro.finalizar_compra()
    if pedido:
        messages.success(request, "¡Compra realizada con éxito!")
        return redirect('perfil')
    else:
        messages.error(request, "Debes iniciar sesión para finalizar la compra.")
        return redirect('login')



