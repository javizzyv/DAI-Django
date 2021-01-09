from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.template import Context, Template
from django import forms
from .models import Libro
from .models import Prestamo

# Create your views here.

# Clase controladora

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = ('libro',)


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('titulo',)


def index(request):
    context = {"formularios": "No"}
    return render(request,'index.html', context)


def formularios(request):
    context = {"formularios": "Si"}
    return render(request,'formularios.html', context)


def mostrar(request):
    form = LibroForm()
    context = {"formularios": "No"}
    return render(request,'mostrar.html', {'form': form})


def editar(request):
    form = LibroForm()
    context = {"formularios": "No"}
    return render(request,'editar.html', {'form': form})


def borrar(request):
    form = LibroForm()
    context = {"formularios": "No"}
    return render(request,'borrar.html', {'form': form})


def aniadir(request):
    form = LibroForm()
    context = {"formularios": "No"}
    return render(request,'aniadir.html', {'form': form})

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)