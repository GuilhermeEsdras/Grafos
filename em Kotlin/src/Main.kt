import Grafo

fun main(args: Array<String>) {

    val grafoK3DeTeste = Grafo(mutableListOf('A', 'B', 'C'), mutableMapOf("a1" to "A-B", "a2" to "A-C", "a3" to "B-C"))
    println("Grafo K3 de Teste:\n$grafoK3DeTeste \n")


    val vertices = mutableListOf('J', 'C', 'E', 'P', 'M', 'T', 'Z')
    val arestas = mutableMapOf( "a1" to "J-C", "a2" to "C-E", "a3" to "C-E", "a4" to "C-P", "a5" to "C-P", "a6" to "C-M",
        "a7" to "C-T", "a8" to "M-T", "a9" to "T-Z")

    val paraiba = Grafo(vertices, arestas)

    println("Grafo da Paraíba:")
    println("Vértices (N): ${paraiba.N}")
    println("Arestas (A): ${paraiba.A}")

    println("2 - a) Pares de Vértices não adjacentes:\n" + paraiba.verticesNaoAdjacentes())
    println("2 - b) Há Vértices Adjacentes a ele mesmo/Laços? - " + if (paraiba.haLaco()) "Sim" else "Não")
    println("2 - c) Há arestas paralelas? - " + if (paraiba.haParalelas()) "Sim" else "Não")
    paraiba.N.forEach {
            vertice ->
        println("2 - d) Grau do vértice ${vertice}: " + paraiba.grau(vertice) )
    }

    val v = 'C'
    println("2 - e) Lista de vértices que incidem sobre o vértice $v da Paraíba: " +
            paraiba.arestasSobreVertice(v))

    println("2 - f) Eh completo? - " + if (paraiba.ehCompleto()) "Sim" else "Não")

}