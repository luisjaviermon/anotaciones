### Comando para exploracion de archivos (ls)
```bash
#mostrar todo el contenido de una ubicacion
ls -la 
#Ordenar el contenido por tamaño
ls -lS
#Ordenar por tamaño y mostrar el tamaño
ls -lSh
#Ordenar de forma descendiente el contenido
ls -lr
```

### Comando para mostrar el contenido en forma de arbol (tree)
~~~bash
tree
#fitrar por nivel de profundidad
tree -L [numero_nivel]
~~~

### Creacion de directorios (mkdir)
~~~bash
mkdir [nombre_directorio1] [nombre_directorio2] [nombre_directorio3] ...
~~~

### Creacion de archivos
~~~bash
touch [nombre_directorio1] [nombre_directorio2] [nombre_directorio3] ...
~~~

__NOTA__: Para crear un archivo o directorio con espacios en el nombre es necesario colocarlo entre comillas (")

### Copiar archivo (cp)
~~~bash
cp [ruta_origen_nombre_archivo] [ruta_destino_nombre_archivo]
~~~

### Mover un archivo (mv)
~~~bash
mv [ruta_origen] [ruta_destino]
#para renombrar un archivo
mv [archivo_nombre_anterior] [archivo_nuevo_nombre]
#NOTA: el comando funciona igual para directorios
~~~

### Eliminar algun elemento (rm)
~~~bash
rm [archivo]

#solicitar confirmacion para elimianr archivo
#NOTA: i es por interactive
rm -i [archivo]

#Elimianr un directorio
#NOTA: la bandera -f es para forzar todos los elementos sin pedir confirmacion 
rm -rfi [directorio]
~~~
__Nota__: Para eliminar un archivo con el uso de la bandera _-i_ se debe colocar "y"

### Explorar el contenido de archivos 
~~~bash
#Muestra las primeras n lineas de un archivo
head [nombre_archivo] -n 15
#Muestra las ultimas n lineas de un archivo
tail [nombre_archivo] -n 20
#Mostrar todo el contenido de forma interactiva
less [nombre_archivo]
#Abrir un archivo con la aplicacion determinada
xdg-open [nombre_archivo]
~~~

## Wildcards
Permiten una busqueda mas eficiente de archivos en base a ciertas caracteristicas

son similares a la aplicacion de expresiones regulares pero para buscar ciertos formatos de archivos

  - cadena* - busca todo lo que llebe en un inicio la palabra cadena
  - cadena? - permite buscar todos los archivos que despues de cadena tengan un solo caracter
  - [] - esta es una busqueda por clases. en las cuales podemos englobar ciertos caracteres especificos
  __NOTA__: dentro de las clases podemos colocar ciertas caracteristicas especiales dentro de la busqueda, por ejemplo:
    
    * [[:upper:]]*: permite buscar archivos que inicien con una letra mayuscula   