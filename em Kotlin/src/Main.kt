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

    println("Lista de Vértices não adjacentes:\n" + paraiba.verticesNaoAdjacentes())
}