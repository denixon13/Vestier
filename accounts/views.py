from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistroForm
from orders.models import Pedido

# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')  # o a donde quieras redirigir
        else:
            return render(request, 'usuarios/registro.html', {'form': form})  # si el form no es válido
    else:
        form = RegistroForm()
        return render(request, 'usuarios/registro.html', {'form': form})  # si es GET
    
@login_required
def perfil_usuario(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'usuarios/perfil.html', {
        'usuario': request.user,
        'pedidos': pedidos
    })