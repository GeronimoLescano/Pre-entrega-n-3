from django.db import models
from django.utils import timezone
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"{self.titulo}-{self.autor}"
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=100, null=True, blank= True )
    
    def __str__(self) -> str:
        return f"{self.nombre}-{self.apellido}+{self.direccion}"
    
class Sucursal(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True, blank=True)
    sucursales = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"{self.sucursales}"

class Biblioteca(models.Model):
   libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
   usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
   sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
   fecha_prestamo = models.DateTimeField(default=timezone.now)
   def __str__(self):
        return f"{self.usuario} toma {self.libro} de {self.sucursal}"
   
