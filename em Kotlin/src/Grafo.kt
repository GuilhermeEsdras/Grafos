class VerticeInvalidoException(messagem: String): Exception(messagem)
class ArestaInvalidaException(mensagem: String): Exception(mensagem)

class Grafo(var N: MutableList<Char>, var A: MutableMap<String, String>) {

    private var qtdMaxDeSeparador: Int = 1
    private var separadorDeArestas: Char = '-'

    init {
        this.N.forEach {
            v -> if ( !(this.verticeValido(v)) ) throw VerticeInvalidoException("O vértice $v é inválido!")
        }

        this.A.values.forEach {
            a -> if ( !(this.arestaValida(a)) ) throw ArestaInvalidaException("A aresta $a é inválida!")
        }
    }

    fun arestaValida(aresta: String): Boolean {

        var qtdSeparador = 0
        for (i in 0 until aresta.length) {
            if (aresta[i] == this.separadorDeArestas) {
                qtdSeparador += 1
            }
        }
        if (qtdSeparador != this.qtdMaxDeSeparador) return false

        val iSeparador = aresta.indexOf(this.separadorDeArestas)
        if ( (iSeparador == 0) or (aresta.lastIndexOf(this.separadorDeArestas) == aresta.length) )
            return false

        if ( !( this.existeVertice(aresta.first()) ) or !( this.existeVertice(aresta.last()) ) )
            return false

        return true
    }

    fun verticeValido(vertice: Char) = when {

        !(vertice.isLetterOrDigit()) -> {
            false
        }

        vertice == this.separadorDeArestas -> {
            false
        }

        else -> true
    }

    fun existeVertice(vertice: Char): Boolean {
        return ( this.verticeValido(vertice) and( this.N.isNotEmpty() ) )
    }

    fun existeAresta(aresta: String): Boolean {

        var existe = false
        if ( this.arestaValida(aresta) ) {
            this.A.forEach {
                k, v -> if (aresta == k) existe = true
            }
        }

        return existe
    }

    fun adicionaVertice(v: Char) {

        if ( this.verticeValido(v) and !(this.existeVertice(v)) ) {
            this.N.add(v)
        } else {
            throw VerticeInvalidoException("O vértice $v é inválido!")
        }

    }

    fun adicionaAresta(nome: String, a: String) {

        if ( this.arestaValida(a) ) {
            this.A[nome] = a
        } else {
            throw ArestaInvalidaException("A aresta ${this.A[a]} é inválida!")
        }

    }

    fun verticesNaoAdjacentes(): Collection<String> {

        val listaDeArestas = this.A.values
        val listaDeVertices = this.N

        var listaDeNaoAdjacentes = mutableListOf<String>()

        listaDeVertices.forEach {
            v1 -> listaDeVertices.forEach {
                    v2 ->
                    val arestaIndo = "$v1${this.separadorDeArestas}$v2"
                    val arestaVindo = "$v2${this.separadorDeArestas}$v1"
                    if ( !(listaDeArestas.contains(arestaIndo)) and !(listaDeArestas.contains(arestaVindo)) )
                        listaDeNaoAdjacentes.add(arestaIndo)
                    }
        }

        return listaDeNaoAdjacentes
    }

    fun testeListaDeArestas() {

        var listaDeArestas = this.A.values

        listaDeArestas.forEach {
            v1 -> println(v1[0])
        }
    }

    override fun toString(): String {

        var grafoStr: String = ""

        this.N.forEachIndexed {
                i, v -> grafoStr += v
            if (i < (this.N.size - 1)) {
                grafoStr += ", "
            }
        }

        grafoStr += "\n"

        this.A.values.forEachIndexed {
                i, a -> grafoStr += a
            if (i < (this.A.size - 1)) {
                grafoStr += ", "
            }
        }

        return grafoStr
    }
}