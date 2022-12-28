from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('administrador/', views.admin_index, name='administrador'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('crearusuario/', views.crearusuario, name='crearusuario'),
    path('editarusuario/', views.editarusuario, name='editarusuario'),
    path('editarusuario/<int:id>', views.editarusuario, name='editarusuario'),
    path('eliminarusuario/<int:id>', views.eliminarusuario, name='eliminarusuario'),
    path('libros/',views.libros, name='libros'),
    path('libros/crearlibro',views.crearlibro, name='crearlibro'),
    path('libros/editarlibro',views.editarlibro, name='editarlibro'),
    path('libros/editarlibro/<int:id>',views.editarlibro, name='editarlibro'),
    path('eliminarlibro/<int:id>',views.eliminarlibro, name='eliminarlibro'),
    path('registro/', views.registro, name='registro'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('salir/', views.salir, name='salir'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)