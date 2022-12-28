from django.shortcuts import render,redirect
from .models import Usuario,Libro
from .forms import UserForm, LibroForm,EditUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

#Acceso a los usuarios
@login_required
@permission_required('admin_index',login_url='ingresar')
def admin_index(request):
    return render(request, 'privado/admin_index.html')

@login_required
@permission_required('usuarios',login_url='ingresar')
def usuarios(request):
    usuarios=Usuario.objects.all()
    return render(request, 'privado/usuarios/index.html', {'usuarios':usuarios})

@login_required
@permission_required('crearusuario',login_url='ingresar')
def crearusuario(request):
    formulario= UserForm(request.POST or None)
    if formulario.is_valid():        
        formulario.save()
        return redirect('usuarios') 
    return render(request, 'privado/usuarios/crear.html',{'formulario':formulario})

@login_required
@permission_required('crearusuario',login_url='ingresar')
def editarusuario(request,id):
    usuario=Usuario.objects.get(id=id)
    formulario=EditUserForm(request.POST or None,instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request, 'privado/usuarios/editar.html', {'formulario':formulario})

@login_required
@permission_required('crearusuario',login_url='ingresar')
def eliminarusuario(request, id):
    usuario=Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')


#Acceso a libros

@login_required
@permission_required('libros',login_url='ingresar')
def libros(request):
    if Usuario.is_superuser:
        libros= Libro.objects.all()
        return render(request, 'privado/libros/index.html',{'libros':libros})
    else:
        return render(request, 'privado/usuarios/login.html')

@login_required
@permission_required('crearusuario',login_url='ingresar')
def crearlibro(request):
    formulario= LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros') 
    return render(request, 'privado/libros/crear.html',{'formulario':formulario})

@login_required
@permission_required('crearusuario',login_url='ingresar')
def editarlibro(request,id):
    libro=Libro.objects.get(id=id)
    formulario=LibroForm(request.POST or None,request.FILES or None,instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'privado/libros/editar.html', {'formulario':formulario})

@login_required
@permission_required('crearusuario',login_url='ingresar')
def eliminarlibro(request, id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')


def registro(request):
    formulario= UserForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('ingresar')
    return render(request, 'privado/usuarios/registro.html',{'formulario':formulario})

def ingresar(request):
    if request.method == 'GET':
        return render(request,'privado/usuarios/ingresar.html',{
        'form':AuthenticationForm
        })
    else:
        usuario=authenticate(
            request,username=request.POST['username'],password=request.POST['password'])
        if usuario is None:
            return render(request,'administrador/usuarios/ingresar.html',{
                'form':AuthenticationForm,
                'error':'Usuario o contraseña es incorrecto'
            })
        else:
            login(request,usuario)
            if usuario.is_superuser:
                return redirect('administrador')
            else:
                return redirect('desclibros')

def salir(request):
    logout(request)
    return redirect('inicio')
