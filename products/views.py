from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria, Subcategoria, AtributoProducto



# Create your views here.

def categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'products/categoria/categorias.html', context)

def categoria_detail(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    subcategorias = Subcategoria.objects.filter(categoria=categoria)
    productos = Producto.objects.filter(categoria=categoria)
    context = {
        'categoria': categoria,
        'subcategorias': subcategorias,
        'productos': productos,
    }
    return render(request, 'products/categoria/categoria_detail.html', context)


def subcategoria_detail(request, subcategoria_id):
    subcategoria = Subcategoria.objects.get(id=subcategoria_id)
    productos = Producto.objects.filter(subcategoria=subcategoria)
    context = {
        'subcategoria': subcategoria,
        'productos': productos,
    }
    return render(request, 'products/subcategoria/subcategoria_detail.html', context)

def productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos,
    }
    return render(request, 'products/productos/productos.html', context)

def producto_detail(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    tallas = AtributoProducto.objects.filter(producto=producto)
    context = {
        'producto': producto,
        'tallas': tallas,
    }
    return render(request, 'products/productos/producto_detail.html', context)

def buscar(request):
    query = request.GET.get('q')
    resultados = Producto.objects.filter(nombre__icontains=query) if query else []
    context = {
        'query': query,
        'resultados': resultados,
    }
    return render(request, 'products/busqueda/resultados.html', context)


