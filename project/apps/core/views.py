from django.shortcuts import render, redirect
from . import models
from . import forms

def index(request):
    context = {"app_name": "Coderhouse"}
    return render(request, "core/index.html", context)

def libro_list(request):
    consulta = models.Libro.objects.all()
    contexto = {"libros": consulta}
    return render(request, "core/libro_list.html", contexto)

def libro_form(request):
    if request.method == "POST":
        form = forms.LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libro_list")

    else:
        form = forms.LibroForm()
    return render(request, "core/libro_form.html", {"form": form})


def usuario_list(request):
    consulta = models.Usuario.objects.all()
    contexto = {"usuarios": consulta}
    return render(request, "core/usuario_list.html", contexto)


def usuario_form(request):
    if request.method == "POST":
        form = forms.UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario_list")

    else:
        form = forms.UsuarioForm()
    return render(request, "core/usuario_form.html", {"form": form})

def sucursal_list(request):
    consulta = models.Sucursal.objects.all()
    contexto = {"sucursales": consulta}
    return render(request, "core/sucursal_list.html", contexto)

def biblioteca_list(request):
    consulta = models.Biblioteca.objects.all()
    contexto = {"bibliotecas": consulta}
    return render(request, "core/biblioteca_list.html", contexto)


def tomar_libro_form(request):
    if request.method == 'POST':
        form = forms.PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biblioteca_list')

    else:
        form = forms.PrestamoForm()

    return render(request, 'core/tomar_libro_form.html', {'form': form})