from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("libro/list", views.libro_list, name='libro_list'),
    path("libro/form", views.libro_form, name='libro_form'),
    path("usuario/list", views.usuario_list, name='usuario_list'),
    path("usuario/form", views.usuario_form, name='usuario_form'),
    path("sucursal/list", views.sucursal_list, name='sucursal_list'),
    path("biblioteca/list", views.biblioteca_list, name='biblioteca_list'),
    path('tomar_libro_form/', views.tomar_libro_form, name='tomar_libro_form'),
    
]


