from django import forms

from . import models
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class LibroForm(forms.ModelForm):
    class Meta:
        model = models.Libro
        fields = "__all__"

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = models.Biblioteca
        fields = ['libro', 'usuario', 'sucursal']
