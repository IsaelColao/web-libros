from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro, Autor
from .forms import LibroForm, AutorForm

#! Todos estos metodos son para desplazarse entre las ventanas

def inicio (request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

#Libro
def libros (request):
    libros = Libro.objects.prefetch_related("autores_ids").all()
    return render (request, "libros/index.html", {'libros' : libros})

def crear_libro (request):
    formulario = LibroForm(request.POST or None , request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render (request, "libros/crear.html", {'formulario' : formulario})

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None , request.FILES or None, instance=libro)
    if formulario.is_valid()and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    
    return render (request, "libros/editar.html", {'formulario' : formulario})

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

#Autor
def autores (request):
    autores = Autor.objects.all()
    return render (request, "autores/index.html", {'autores' : autores})

def crear_autor (request):
    formulario = AutorForm(request.POST or None , request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('autores')
    return render (request, "autores/crear.html", {'formulario' : formulario})

def editar_autor(request, id):
    autor = Autor.objects.get(id=id)
    formulario = AutorForm(request.POST or None , request.FILES or None, instance=autor)
    if formulario.is_valid()and request.method == 'POST':
        formulario.save()
        return redirect('autores')
    
    return render (request, "autores/editar.html", {'formulario' : formulario})

def eliminar_autor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('autores')