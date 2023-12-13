import re


class Interprete:
    def __init__(self):
        self.hechos = {}
        self.reglas = {}

        # Definición de la expresión regular para un átomo
        atomo_pattern = r"^[a-z][a-zA-Z0-9]*$"
        self.atomo_regex = re.compile(atomo_pattern)

        # Definición de la expresión regular para una variable
        variable_pattern = r"^[A-Z][a-zA-Z0-9]*$"
        self.variable_regex = re.compile(variable_pattern)

    # Descompone las estructuras de una expresión
    def descomposicion(self, expresion):
        elementos = expresion[expresion.find("(")+1:expresion.rfind(")")]

        lista_elementos = []
        temp = ''
        contador = 0
        for char in elementos:
            if char == '(':
                contador += 1
            elif char == ')':
                contador -= 1
            elif char == ',' and contador == 0:
                lista_elementos.append(temp.strip())
                temp = ''
                continue
            temp += char
        lista_elementos.append(temp.strip())

        return lista_elementos

    # Comprueba si una expresión es válida
    def es_expresion(self, expresion):
        if self.atomo_regex.match(expresion):
            return True

        if self.variable_regex.match(expresion):
            return True

        atomo, resto = expresion.split('(', 1)
        resto = '(' + resto

        if not self.atomo_regex.match(atomo):
            return False

        if not resto.endswith(')'):
            return False

        estructura = self.descomposicion(resto)

        for elemento in estructura:
            if not self.es_expresion(elemento):
                return False

        return True

    # Comprueba si una expresión es un hecho
    def es_hecho(self, expresion):
        atomo, resto = expresion.split('(', 1)
        resto = '(' + resto

        atomos = self.descomposicion(resto)
        for ato in atomos:
            if not self.atomo_regex.match(ato):
                return False
        return True

    def definir(self, entrada):
        predicados = re.findall(r'\b\w+\([^)]*\)', entrada)
        if len(predicados) <= 1:
            if self.atomo_regex.match(entrada):
                if (entrada in self.hechos) and len(self.hechos[entrada][0]) != 0:
                    print(
                        "La expresión no es válida, intente de nuevo, la cantidad de argumentos es incorrecta, intente de nuevo")
                    return
                self.hechos[entrada] = [[]]
                return
            if self.variable_regex.match(entrada):
                print("La expresión no es válida, intente de nuevo")
                return
            if not self.es_expresion(entrada):
                print("La expresión no es válida, intente de nuevoff")
                return
            if not self.es_hecho(entrada):
                print("La expresión no es un hecho, intente de nuevoff")
                return
            atomo, resto = entrada.split('(', 1)
            resto = '(' + resto
            if atomo in self.hechos:
                resto = resto.strip('()').split(', ')
                if len(resto) != len(self.hechos[atomo][0]):
                    print(
                        "La expresión no es válida, cantidad de argumentos incorrecta, intente de nuevo")
                    return
                self.hechos[atomo].append(resto)
                return
            resto = resto.strip('()').split(', ')
            self.hechos[atomo] = [resto]
        else:
            # Definición de una regla
            antecedente = predicados.pop(0)

            if not self.es_expresion(antecedente):
                print("La expresión no es válida, intente de nuevo")
                return

            for predicado in predicados:
                if not self.es_expresion(predicado) or self.variable_regex.match(predicado):
                    print(
                        "La expresión no es válida o es una variable, intente de nuevo")
                    return
            self.reglas[antecedente] = predicados

    def preguntar(self, expresion):

        if not self.es_expresion(expresion):
            print("La expresión no es válida, intente de nuevo")
            return

        atomo, resto = expresion.split('(', 1)
        resto = '(' + resto
        resto = resto.strip('()').split(', ')

        if self.es_hecho(expresion):
            if atomo in self.hechos.keys():
                if resto in self.hechos[atomo]:
                    print("Satisfacible")
        else:
            if atomo in self.reglas.keys():
                nato = []
                for x in resto:
                    for i in len(self.reglas[atomo]-1):
                        if x in self.reglas[atomo]:
                            print("Satisfacible")
                            return


def main():
    interprete = Interprete()
    while True:
        entrada = input("Ingrese una expresión: ")
        if entrada.startswith("DEF"):
            _, expresion = entrada.split(' ', 1)
            interprete.definir(expresion)
            print(interprete.hechos)
            print(interprete.reglas)
        elif entrada.startswith("ASK"):
            _, expresion = entrada.split(' ', 1)
            interprete.preguntar(expresion)
        elif entrada.startswith("SALIR"):
            break
        else:
            print("La expresión no es válida, intente de nuevo")


if __name__ == "__main__":
    main()
