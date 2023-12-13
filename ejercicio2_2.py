import os
import threading

# Se crea una variable global para almacenar el total de archivos
total = 0
# Se crea un candado para evitar que se acceda a la variable total al mismo tiempo
candado = threading.Lock()


def contar_archivos(path):
    # Inicializar el contador de archivos
    global total
    # Recorrer el directorio y sus subdirectorios
    for raiz, dirs, archivos in os.walk(path):

        with candado:
            total += len(archivos)

        # Crear un hilo para cada subdirectorio
        for direc in dirs:
            hilo = threading.Thread(target=contar_archivos, args=(direc,))
            hilo.start()
            hilo.join()
    return total


path = input("Ingrese la ruta del directorio: ")
print("Cantidad de archivos: ", contar_archivos(path))
