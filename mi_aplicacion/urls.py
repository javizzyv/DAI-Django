# mi_aplicacion/urls.py

from django.urls import include,path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('index', views.index, name='index'),
  path('formularios', views.formularios, name='formularios'),
  path('mostrar', views.mostrar, name='mostrar'),
  path('editar', views.editar, name='editar'),
  path('borrar', views.borrar, name='borrar'),
  path('aniadir', views.aniadir, name='aniadir'),
  path('signup', views.signup, name='signup'),
  path('prestamos', views.prestamos, name='prestamos'),
  path('pedir', views.pedir, name='pedir'),
  path('devolver', views.devolver, name='devolver'),
  path('test_template', views.test_template, name='test_template'),
]