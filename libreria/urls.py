from django.urls import path
from . import views

from django.conf import settings

urlpatterns = [
    path('',views.inicio , name='inicio'),
    path('nosotros', views.nosotros , name='nosotros'),
    path('libros', views.libros , name='libros'),
    path('libros/crear', views.crear_libro , name='crear'),
    path('libros/editar', views.editar_libro , name='editar'),
    path('eliminar/<int:id>', views.eliminar_libro , name='eliminar'),
    path('libros/editar/<int:id>', views.editar_libro , name='editar'),
    
    path('autores', views.autores , name='autores'),
    path('autores/crear', views.crear_autor , name='crear_autor'),
    path('autores/editar', views.editar_autor , name='editar_autor'),
    path('autores/eliminar/<int:id>', views.eliminar_autor , name='eliminar_autor'),
    path('autores/editar/<int:id>', views.editar_autor , name='editar_autor')
]