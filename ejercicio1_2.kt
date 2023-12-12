import java.util.ArrayDeque

// Clase grafo
class grafo {
    var arcos = mutableMapOf<Int, MutableList<Int>>()

    // función que retorna los arcos de un nodo
    fun ontenerArcos(nodo: Int): MutableList<Int> {
        return arcos[nodo] ?: mutableListOf()
    }
}

// Clase abstracta busqueda
abstract class busqueda() {
    abstract fun buscar(desde: Int, hasta: Int): Int
}

// Clase DFS
class DFS(val grafo: grafo) : busqueda() {
    // Sobreescritura del método buscar
    override fun buscar(desde: Int, hasta: Int): Int {
        var pila = ArrayDeque<Int>()
        var visitados = mutableSetOf<Int>()
        // Se coloca 1 porque el nodo inicial ya se cuenta como explorado
        var explorados = 1

        pila.add(desde)

        while (pila.isNotEmpty()) {
            val nodo = pila.pop()

            if (nodo == hasta) {
                return explorados
            }

            if (nodo !in visitados) {
                visitados.add(nodo)
                explorados += 1

                for (arco in grafo.ontenerArcos(nodo)) {
                    pila.push(arco)
                }
            }
        }
        return -1
    }
}

// Clase BFS
class BFS(val grafo: grafo) : busqueda() {
    // Sobreescritura del método buscar
    override fun buscar(desde: Int, hasta: Int): Int {
        var cola = ArrayDeque<Int>()
        var visitados = mutableSetOf<Int>()
        // Se coloca 1 porque el nodo inicial ya se cuenta como explorado
        var explorados = 1

        cola.add(desde)

        while (cola.isNotEmpty()) {
            val nodo = cola.pop()

            if (nodo == hasta) {
                return explorados
            }

            if (nodo !in visitados) {
                visitados.add(nodo)
                explorados += 1

                for (arco in grafo.ontenerArcos(nodo)) {
                    cola.add(arco)
                }
            }
        }
        return -1
    }
}
