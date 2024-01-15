# Pre-entrega-n-3

## Nombre
Link en GitHub: https://github.com/GeronimoLescano/Pre-entrega-n-3.git
Nombre y apellido: Geronímo Lescano
Link de LinkeIn: www.linkedin.com/in/geronimo-lescano-049809196
## Resumen del proyecto
 En el presente proyecto se creo una bibloteca virtual, donde los usuarios pueden ingresar y visualizar los siguientes tipos de datos:
 -Registrar nuevos libros con sus respectivos autores.
 -Registrar nuevos usuarios con sus nombres, apellidos, emails y direcciones.
 -Registrar nuevas sucursales en el país.
 Ademas cuenta con la funcion de tomar un libro, esta funcion registra la fecha, el nombre, libro y la sucursal.
 ## Metodología de creacion
 Se inicio creando un repositorio en GitHub, luego se clono el mismo en el servidor local y se prosiguio a abrirlo a travez de visual studio code.
 ### Desarrollo
    Una vez realizado esto se continuo con:
        -Instalacion de espacio virtual y su activacion.
        -Creacion de carpeta de projectos con la instalacion de Django
        -Creacion de archivo de tipo requirements.txt.
        -Creacion de App dentro de la carpeta Project y dentro de la misma se creo la aplicacion "core".
        -Se creo models(Libro, Usuario, Bibloteca, Sucursal) y ademas se importo la libreria timezone.
        -Creacion y luego una posterior migracion de Models.
        -Creacion de visualizaciones de tipo form y list (en una primera instancia luego fueron cambiados a formato table) con importaciones de render, redirect, forms y models.
        -Creacion de urls para cada visualizacion.
        -Creacion de templates para cada visaulizacion con un tronco principal "base" y una ramificacion centralizada en "Index" como menu principal, luego los templates siguientes heredan de base.
### Concluciones: 
    Si bien costo mucho su desarrollo, hubiron muchos errores tipograficos, se logro concluir la actividad. Lo anterior solo es un pequeño resumen de lo que se realizo.

#### Ejecucion de web en servidor:
    Nos colocamos en nuestra terminal de Visual Studio Code y procedemos a poner el siguiente codigo "python manage.py runserver". 

 



 

 