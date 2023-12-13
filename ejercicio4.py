# Clase que maneja la tabla de metodos virtuales
class Manejador:
    def __init__(self):
        self.clases = []
        self.tablas_metodos = {}

    # Crea una tabla de metodos virtuales para una clase
    def crear_tabla(self, clase, metodos, tabla_superclase={}):
        tabla = tabla_superclase.copy()
        for metodo in metodos:
            tabla[metodo] = clase
        return tabla

    # Agrega una clase a la tabla de metodos virtuales
    def agregar_clase(self, clase, metodos, superclase):
        if clase in self.clases:
            print("La clase ya existe")
            return

        if superclase != None and superclase not in self.clases:
            print("La superclase no existe")
            return

        if len(metodos) != len(set(metodos)):
            print("Existen metodos repetidos")
            return

        self.clases.append(clase)
        if superclase == None:
            self.tablas_metodos[clase] = self.crear_tabla(clase, metodos)
        else:
            self.tablas_metodos[clase] = self.crear_tabla(
                clase, metodos, self.tablas_metodos[superclase])

    # Mostar la tabla de metodos virtuales de una clase
    def mostrar_tabla(self, clase):
        if clase not in self.clases:
            print("La clase no existe")
            return
        for metodo, clase in self.tablas_metodos[clase].items():
            print(metodo, " -> ", clase, " ::", metodo)

# Funcion principal


def main():
    manejador = Manejador()
    while True:
        accion = input(
            "Ingrese una acción (CLASS <tipo> [<nombre>], DESCRIBIR <nombre>, SALIR): ")
        if accion.startswith("CLASS"):
            _, clase, *metodos = accion.split()
            superclase = None
            if ":" in metodos[0]:
                metodos.pop(0)
                superclase = metodos.pop(0)
            manejador.agregar_clase(clase, metodos, superclase)

        elif accion.startswith("DESCRIBIR"):
            _, clase = accion.split()
            manejador.mostrar_tabla(clase)

        elif accion.startswith("SALIR"):
            break

        else:
            print("La acción no es válida, intente de nuevo")


if __name__ == "__main__":
    main()
