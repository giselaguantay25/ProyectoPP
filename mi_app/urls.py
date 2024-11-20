from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuestra_historia/', views.nuestra_historia, name='nuestra_historia'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('recuperar_contraseña/', views.recuperar_contraseña, name='nueva contraseña'),
    path('administracion/', views.administracion, name='administracion'),
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('lista_profesor/', views.lista_profesor, name='lista_profesor'),
    path('lista_competencia/', views.lista_competencia, name='lista_competencia'),
    path('lista_categoria', views.lista_categoria, name='lista_categoria'),
    path('lista_clase/', views.lista_clase, name='lista_clase'),
    path('lista_turno/', views.lista_turno, name='lista_turno'),
    path('lista_cuota/', views.lista_cuota, name='lista_cuota'),
    path('lista_caballo/', views.lista_caballo, name='lista_caballo'),
    path('agregar_alumno/', agregar_alumno, name='agregar_alumno'),
    path('perfil_profe/', perfil, name='perfil_profe'),
    ]