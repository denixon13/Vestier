from .models import Producto, Categoria
from django.shortcuts import render

def categoria_context(request):
    """
    Context processor to add categories to the context.
    """
    categorias = Categoria.objects.all()
    return {
        'categorias': categorias,
    }

def productos_context(request):
    """
    Context processor to add products to the context.
    """
    productos = Producto.objects.all()
    return {
        'productos': productos,
    }