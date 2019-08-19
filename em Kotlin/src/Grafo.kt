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

        val listaDeNaoAdjacentes = mutableListOf<String>()

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

    fun haLaco(): Boolean {

        val listaDeArestas = this.A.values

        listaDeArestas.forEach {
                vertice ->
            if ( vertice[0] == vertice[2] )
                return true
        }

        return false
    }

    fun haParalelas(): Boolean {

        val listaDeArestas = this.A.values
        val sep = this.separadorDeArestas

        val arestaIndoVerificadas = mutableListOf<String>()
        val arestaVindoVerificadas = mutableListOf<String>()

        listaDeArestas.forEach { aresta ->
            val arestaIndo = "${aresta[0]}$sep${aresta[2]}"
            val arestaVindo = "${aresta[2]}$sep${aresta[1]}"

            if ((arestaIndoVerificadas.contains(arestaIndo)) or (arestaVindoVerificadas.contains(arestaVindo))) {
                return true
            } else {
                arestaIndoVerificadas.add(arestaIndo)
                arestaVindoVerificadas.add(arestaVindo)
            }
        }

        return false
    }

    fun grau(v: Char): Int {

        val listaDeArestas = this.A.values
        var grau: Int = 0

        listaDeArestas.forEach {
                vertice ->
            if ( (vertice[0] == v) or (vertice[2] == v) )
                grau++
        }

        return grau
    }

    fun arestasSobreVertice(v: Char): MutableCollection<String> {

        val listaDeArestas = this.A
        val arestasSobreV = mutableListOf<String>()

        for ( (aresta, vertice) in listaDeArestas ) {
            if ( (vertice[0] == v) or (vertice[2] == v) )
                arestasSobreV.add(aresta)
        }

        return arestasSobreV
    }

    fun ehCompleto(): Boolean {

        val listaDeVertices = this.N
        val listaDeArestas = this.A.values

        val n = listaDeVertices.size

        if (n == 1) return true

        val maxDeArestas: Int = (n * (n - 1)) / 2

        val arestasVerificadas = mutableListOf<String>()

        listaDeArestas.forEach { vertice ->
            val verticeContrario = "$vertice[2]$vertice[1]$vertice[0]"

            if ((arestasVerificadas.contains(vertice)) or (arestasVerificadas.contains(verticeContrario))) {
                return false
            } else {
                arestasVerificadas.add(vertice)
            }
        }

        return ( (arestasVerificadas.size == maxDeArestas) or (arestasVerificadas.size == 2) )
    }

    fun testeListaDeArestas() {

        val listaDeArestas = this.A.values

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