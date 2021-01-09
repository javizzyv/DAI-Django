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
  path('test_template', views.test_template, name='test_template'),
]