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
### eliminar un ambiente
