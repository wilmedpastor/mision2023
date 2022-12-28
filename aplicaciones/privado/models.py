import os
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser): 
    email=models.EmailField(verbose_name='Correo Electrónico',max_length=100,unique=True)
    phone=models.CharField(max_length=12,verbose_name='Celular')     

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=100,verbose_name='Titulo')
    imagen= models.ImageField(upload_to='aplicaciones/static/img/',verbose_name='Imagen',null=True)
    descripcion= models.TextField(verbose_name='Descripcion',null=True)
    url= models.CharField(verbose_name='url',max_length=100, null=True)

    def __str__(self):        
        return self.titulo

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen.path):
            self.imagen.storage.delete(self.imagen.path)
        super(Libro, self).delete(*args, **kwargs)

