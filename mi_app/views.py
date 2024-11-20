from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')
def nuestra_historia(request):
    return render(request, 'nuestra_historia.html')
def servicios(request):
    return render(request, 'servicios.html')
def contacto(request):
    return render(request, 'contacto.html')
def ubicacion(request):
    return render(request, 'ubicacion.html')
def iniciar_sesion(request):
    return render(request, 'Inicio de seccion.html')
def recuperar_contraseña(request):
    return render(request, 'RecuperaciondeContraseña.html')
def confirmar_codigo(request):
    return render(request, 'Codigo de recuperacion.html')
def nueva_contraseña(request):
    return render(request, 'nueva contraseña.html')
def administracion(request):
    return render(request, 'administracion.html')
def perfil(request):
    return render(request, 'perfil_profe.html')
def lista_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})
def lista_profesor(request):
    profesores = Profesor.objects.all()
    return render(request, 'lista_profesores.html', {'profesores': profesores})

def lista_competencia(request):
    competencias = Competencia.objects.all()
    return render(request, 'lista_competencias.html', {'competencias': competencias})

def lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def lista_clase(request):
    clases = Clase.objects.all()
    return render(request, 'lista_clases.html', {'clases': clases})

def lista_turno(request):
    turnos = Turno.objects.all()
    return render(request, 'lista_turnos.html', {'turnos': turnos})

def lista_cuota(request):
    cuotas = Cuota.objects.all()
    return render(request, 'lista_cuotas.html', {'cuotas': cuotas})

def lista_caballo(request):
    caballos = Caballo.objects.all()
    return render(request, 'lista_caballos.html', {'caballos': caballos})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')  # Redirigir a la lista de alumnos
    else:
        form = AlumnosForm()
    return render(request, 'agregar_alumno.html', {'form': form})