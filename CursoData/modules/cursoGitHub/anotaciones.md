# Curso Git Hub
---
### Git
Git es un sistema de control de versiones. Esto es que en lugar de guardar toda una version de cierto archivo, lo que se guarda en realidad son los cambios hechos en el, de tal forma que se puede regresar a cierto punto para poder ver el estado de este archivo e incluso comparar entre puntos en el tiempo

Como nota se debe evitar el incluir binarios dentro de un repo, ya que por minimo que sea el cambio, el binario se debe de guardar completo, por lo cual es considerado una mala practica. Para guardar archivos binario se recomienda hacerlo en un CND.

![InfografiaQueEsGit](./img/InfografiaQueEsGit.jpg "Que es git")

### Iniciar un repositorio
Para iniciar un repositorio es necesario tener contemplada la carpeta principal de nuestro proyecto, luego posicionado en nuestra carpeta usamos el comando `git init`. Al ejecutar el comando, en automatico se crea la carpeta .git.

### Estado de un repositorio
Para saber el estado de un repo (la rama, los cambios, etc) se usa el comando `git status`. para añadir los cambios a la historia del repo usamos 
~~~bash
git add [rutaArchivo]|.
~~~

### Eliminar un archivo del historial
Para eliminar un archivo usamos
~~~bash
#elimina el registro de la base pero lo regresa a como estaba antes del add
git rm --cached [rutaArchivo]
~~~

Al momento de usar el comando add se llega a una fase en git llamada _stage_. Se podria considerar el intermedio entre un nuevo archivo y su inclusion en la base de cambios

### Confirmar cambios
Para confirmar los cambios con el fin de poder añadir los cambios usamos `git commit`. Como buena practica se recomienda añadir comentarios.
~~~bash
git commit -m "[comentarioSobreElCambio]"
~~~

### Configuracion de git
La primera vez que se usa git no se tiene conocimiento de quien esta realizando los cambios, por lo cual se debe de configurar esto, para lo cual usamos el comando `git config`
~~~bash
#Muestra todos las configuraciones y sus valores actuales
git config --list

#Ver donde se encuentran almacenadas las configuraciones
git config --list --show-origin

#Colocar un valor de configuracion de forma global
git config --global [configuracion] "[valor]"
~~~

### Historial de cambios
Para ver los cambios hechos en una seccion en especifico usamos el comando `git log`
~~~bash
git log [archivo]
~~~

__NOTA__: El primer registro que arroja el comando es el cambio mas reciente

### Comarar los cambios en las versiones
Para ver los cambios entre las ultimas dos versiones se usa el comando `git show` mas el archivo de interes

Si se desea comparar entre dos versiones arbitrarias se usa `git diff`
~~~bash
git diff [versionOriginal] [versionMasNueva]
~~~