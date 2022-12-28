from django import forms
from .models import Usuario,Libro
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

#class UserForm(forms.ModelForm):

class UpperField(forms.CharField):
    def to_python(self,value):
        return value.upper()

class UserForm(UserCreationForm):   
    class Meta:
        model = Usuario        
        fields = ('username','first_name','last_name','email','phone')
        

class EditUserForm(UserChangeForm):   
    class Meta:
        model = Usuario               
        fields = ('first_name','last_name','email','phone') 

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

#ENLACE PARA DESCARGAR ARCHIVOS DE GOOGLE DRIVE DIRECTAMENTE, SOLO CAMBIAR EL ID: https://drive.google.com/u/0/uc?id=0B8lK02sZ8njTdkZhN3hTYS1uSDg&export=download 
