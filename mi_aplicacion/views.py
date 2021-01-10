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
        fields = ('libro','fecha','usuario',)


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('titulo',)


class LibroFormExt(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('titulo','autor',)


def index(request):
    context = {"formularios": "No"}
    return render(request,'index.html', context)


def formularios(request):
    libros = Libro.objects.all()
    #libro = Libro.objects.filter(titulo="El Pistolero")
    libro = ''
    return render(request,'formularios.html', {"formularios": "Si", "libros": libros, "libro": libro})


def mostrar(request):
    context = {"formularios": "No"}

    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            #libroT = form.save(commit=True)
            libro = Libro.objects.filter(titulo=form.cleaned_data.get("titulo"))

            if libro:
                exito = 'Si'
                return render(request,'formularios.html', {"libro": libro[0], "formularios": "Si", "libros": "", "Individual": "Si", "exito": exito})
            else:
                libro = ''
                error = 'Not exists'
                form = LibroForm()
                return render(request,'mostrar.html', {"libro": libro, "formularios": "No", "libros": "", "Individual": "Si", "error": error, "form": form})

            
    else:
        form = LibroForm()
        return render(request,'mostrar.html', {'form': form})


def editar(request):
    if request.method == "POST":
        formAc = request.POST
        form = LibroFormExt((request.POST))
        if form.is_valid():
            
            libro = Libro.objects.filter(titulo=formAc.get("tituloActual"))

            if libro:
                exito = 'Si'
                libro.update(titulo=form.cleaned_data.get("titulo"), autor=form.cleaned_data.get("autor"))
                libro = Libro.objects.filter(titulo=form.cleaned_data.get("titulo"))
                return render(request,'formularios.html', {"libro": libro[0], "formularios": "Si", "libros": "", "Individual": "Si", "exito": exito})
            else:
                libro = ''
                error = 'Not exists'
                form = LibroFormExt()
                return render(request,'editar.html', {"libro": libro, "formularios": "No", "libros": "", "Individual": "Si", "error": error, "form": form})

            
    else:
        form = LibroFormExt()
        return render(request,'editar.html', {'form': form})


def borrar(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            
            libro = Libro.objects.filter(titulo=form.cleaned_data.get("titulo"))
            

            if libro:
                libro.delete()
                libro = ''
                libros = Libro.objects.all()
                exito = 'Si'
                return render(request,'formularios.html', {"libro": libro, "formularios": "Si", "libros": libros, "Individual": "Si", "exito": exito})
            else:
                libro = ''
                error = 'Not exists'
                form = LibroForm()
                return render(request,'borrar.html', {"libro": libro, "formularios": "No", "libros": "", "Individual": "Si", "error": error, "form": form})

            
    else:
        form = LibroForm()
        return render(request,'borrar.html', {'form': form})


def aniadir(request):
    if request.method == "POST":
        form = LibroFormExt(request.POST)
        if form.is_valid():
            #libroT = form.save(commit=True)
            libro = Libro.objects.filter(titulo=form.cleaned_data.get("titulo"))
            
            if not libro:
                form.save(commit=True)
                libro = Libro.objects.filter(titulo=form.cleaned_data.get("titulo"))
                exito = 'Si'
                return render(request,'formularios.html', {"libro": libro[0], "formularios": "Si", "libros": "", "Individual": "Si", "exito": exito})
            else:
                libro = ''
                error = 'Already exists'
                form = LibroFormExt()
                return render(request,'aniadir.html', {"libro": libro, "formularios": "No", "libros": "", "Individual": "Si", "error": error, "form": form})

            
    else:
        form = LibroFormExt()
        return render(request,'aniadir.html', {'form': form})

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)