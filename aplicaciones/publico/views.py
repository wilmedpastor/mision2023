from django.shortcuts import render
from aplicaciones.privado.models import Libro


# Create your views here.

def home(request):
    return render(request, 'publico/inicio.html')

def eventos(request):
    return render(request, 'publico/eventos.html')

def contacto(request):
    return render(request, 'publico/contacto.html')

def pastores(request):
    return render(request, 'publico/pastores.html')

def ministerios(request):
    return render(request, 'publico/ministerios.html')

def doctrina(request):
    return render(request, 'publico/doctrina.html')

def misionvision(request):
    return render(request, 'publico/misionvision.html')

def servicios(request):
    return render(request, 'publico/servicios.html')

def videoanuncios(request):
    return render(request, 'publico/videoanuncios.html')

def desclibros(request):
    libros= Libro.objects.all()
    return render(request, 'publico/desclibros.html',{'libros':libros})



