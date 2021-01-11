from django.shortcuts import render, HttpResponse, redirect
from django.template import Context, Template
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django import forms
from .models import Libro
from .models import Prestamo
from django.contrib.auth.models import User

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



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def prestamos(request):
    prestamos = Prestamo.objects.filter(usuario=request.user.id)
    return render(request, 'prestamos.html', {"prestamos":prestamos})


def pedir(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            #libroT = form.save(commit=True)
            print(form.cleaned_data.get("titulo"))
            libroP = Libro.objects.filter(titulo=form.cleaned_data.get("titulo"))
            print(libroP)

            if libroP[0] and not Prestamo.objects.filter(libro=libroP[0]):
                exito = 'Si'
                print(exito)
                Prestamo.objects.create(libro=libroP[0], usuario=request.user)
                #formPrestamo.libro = libroP
                #formPrestamo.usuario = request.user
                #formPrestamo.save(commit=True)
                prestamos = Prestamo.objects.filter(usuario=request.user.id)
                return render(request,'prestamos.html', {"exito": exito, "prestamos":prestamos})
            else:
                error = 'Not exists'
                form = LibroForm()
                return render(request,'pedir.html', {"error": error, "form": form})

            
    else:
        form = LibroForm()
        return render(request,'pedir.html', {'form': form})


def devolver(request):
    if request.method == 'POST':
        form = request.POST
        libroDevolver = Libro.objects.filter(titulo=form.get("libro"))
        prestamo = Prestamo.objects.filter(libro=libroDevolver[0])
        prestamo.delete()
        exito = 'Si'
        prestamos = Prestamo.objects.filter(usuario=request.user.id)
        return render(request, 'prestamos.html', {"exito":exito, "prestamos":prestamos})

    return render(request, 'prestamos.html')


def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)



# staff pass : UGRDAIPRACTICAS
# staff usuarios: Leo, Javi, Isma

# user prueba : UserPrueba, UsuarioPrueba, UserPrueba1234
# user pass : Contrasenia1234

# admin : admin
# pass : UGRDAIPRACTICAS