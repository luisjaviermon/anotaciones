### lista de ambientes disponibles
```bash
conda env list
```

### Crear un nuevo ambiente
```bash
conda create --name [nombre_ambiente] [dependencia1]=[version] [dependencia2]=[version] ... 
```

NOTA: Si no se coloca la versión se va a instalar la mas actual

### Activar un ambiente
```bash
conda activate [ambiente]
```

### Desactivar un paquete
```bash
conda deactivate
```
### Verificar la lista de paquetes instalados
```bash
conda list <paquete>
``` 

### Actualizar un paquete
```bash
conda update [paquete]
```

### Instalar una version especifica de qun paquete
```bash
conda install [paquete1]=[version] [paquete2]=[version]
```

### Crear un ambiente que copia la configuracion de otro
```bash
conda create --bame [nombre_base_destino] --copy --clone [nombre_base_origen]
```
### eliminar un paquete o dependencia
 ```bash
 conda remove [paquete]
 ```

 ### Eliminar un ambiente
 ```bash
 conda env remove --name|-n [ambiente]
 ```

 NOTA: un ambiente en uso no se puede eliminar. es necesario desactivarlo

### Instalar paquetes desde un canal en especifico
Un canal es la pagina de la cual se puede descargar un paquete o dependencia. 
```bash
conda install --channel [canal] [paquete]
```

Para buscar el paquete en un canal se accede a https://anaconda.org/

### Uso de revisiones
Las revisiones son registros de los cambios hechos en el ambiente, que paquetes se instalaron o se quitaron. 

### Ver lista de revisiones
```bash
conda list --revision
```

### Regresar a una cierta revision en especifico
```bash
conda install --revision [numero_revision]
```

### Exportar un ambiente y colocarlo en un archivo
```bash
conda env export --no-builds|--from-history --file [nombre_archivo]
```

### Instalar un ambiente exportado
```bash
conda env create --file [ruta_archivo]
```
NOTA: La extension para poder instalar ambientes desde archivo es .yml

### Mamba
Mamba es una optimizacion que permite la creacion y resolucion de dependencias en forma paralela, esto con el fin de hacerlo mas rapido. Para instalar mamba usamos 

```bash
conda install --channel conda-forge mamba
```

### Divide y venceras
Es el uso de la estrategia en la cual se divide una gran tarea en tareas mas pequeñas.
Dentro de el uso de ambientes es posible el dividir las dependencias en ambientes distintos con el fin de que si es necesario actualizar algun paquete, los demas no se vean afectados con esta actualizacion.
Una herramienta muy util en anaconda para poder ejecutar un proyecto con distintos ambientes es snakemate