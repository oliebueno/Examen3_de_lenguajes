import kotlin.Boolean

abstract class Secuencia<T> {
    // Metodo para agregar un elemento a la secuencia
    abstract fun agregar(elemento: T)
    // Metodo para remover un elemento de la secuencia
    abstract fun remover(): T
    // Metodo que indica si una secuencia esta vacia
    abstract fun vacio(): Boolean
}

// Clase que implementa una Pila
class Pila<T> : Secuencia<T>() {
    // Lista que almacena los elementos de la pila
    private val elementos = mutableListOf<T>()

    // Metodo para agregar un elemento a la pila
    override fun agregar(elemento: T) {
        elementos.add(0, elemento)
    }

    // Metodo para remover un elemento de la pila
    override fun remover(): T {
        if (vacio()) {
            throw Exception("La pila esta vacia")
        }
        return elementos.removeAt(0)
    }

    // Metodo que indica si la pila esta vacia
    override fun vacio(): Boolean {
        return elementos.isEmpty()
    }

    // Función extra para imprimir la pila
    fun imprimir() {
        println(elementos)
    }
}

// Clase que implementa una Cola
class Cola<T> : Secuencia<T>() {
    // Lista que almacena los elementos de la cola
    private val elementos = mutableListOf<T>()

    // Metodo para agregar un elemento a la cola
    override fun agregar(elemento: T) {
        elementos.add(elemento)
    }

    // Metodo para remover un elemento de la cola
    override fun remover(): T {
        if (vacio()) {
            throw Exception("La cola esta vacia")
        }
        return elementos.removeAt(0)
    }

    // Metodo que indica si la cola esta vacia
    override fun vacio(): Boolean {
        return elementos.isEmpty()
    }

    // Función extra para imprimir la cola
    fun imprimir() {
        println(elementos)
    }
}
