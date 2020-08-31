# lab2-redes

## Instrucciones de uso

### Ejecutar archivo de codificación

El archivo txt a utilizar debe estar en la carpeta inputs/codificacion/
Se puede otorgar como parámetro el txt a utilizar en caso de no otorgar parámetro con txt a utilizar se intenta usar por defecto el nombre 'mensaje.txt'

- Ejemplo: python src/codificacion.py archivo.txt

### Ejecutar arhivo de simulación de ruido

Lee archivo 'codificación-enviada.txt' ubicado en carpeta outputs/codificacion, generado con la ejecución previa del script 'codificacion.py'. Escribe salida en carpeta inputs/decodificacion en archivo 'codificación-recibida.txt' .

- Ejemplo: python src/simulacion-ruido.py

### Ejecutar archivo de decodificación

Se puede otorgar como  parametro el nombre que tendrá el txt de salida. El txt de salida será ubicado en la carpeta output/decodificacion.

- Ejemplo: python src/decodificacion.py resultado.txt