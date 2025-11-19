from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'appvestier/home.html', {})

def politica(request):
    return render(request, 'appvestier/politica.html', {})

