from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='equipo')
    escudo = models.ImageField(upload_to='imagenes/',verbose_name='escudo', null=True)
    descripcion = models.TextField(verbose_name='descripcion', null=True)
    
    def __str__(self):
        fila = "nombre: " + self.nombre + " - " + "descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parent=False):
        self.escudo.storage.delete(self.escudo.name)
        super().delete()
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} Perfil'    