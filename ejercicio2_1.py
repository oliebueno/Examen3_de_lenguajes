import concurrent.futures

# Funcion que calcula el producto escalar de dos vectores de forma concurrente


def producto(a, b):
    total = 0
    with concurrent.futures.ThreadPoolExecutor() as ejecutor:
        memoria = []
        for i in range(len(a)):
            memoria.append(ejecutor.submit(lambda x: a[x] * b[x], i))
        for future in concurrent.futures.as_completed(memoria):
            total += future.result()
    return total


# Entrada del usuario y salida del resultado
a = input("Ingrese el primer vector separado por comas: ")
a = [int(x) for x in a.split(",")]
b = input("Ingrese el segundo vector separado por comas: ")
b = [int(x) for x in b.split(",")]
print("El resultado es: ", producto(a, b))
