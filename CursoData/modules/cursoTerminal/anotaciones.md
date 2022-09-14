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

