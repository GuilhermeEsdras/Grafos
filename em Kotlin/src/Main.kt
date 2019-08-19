fun main(args: Array<String>) {

    val vertices = mutableListOf('A', 'B', 'C')
    val arestas = mutableMapOf("a1" to "A-B", "a2" to "A-C", "a3" to "B-C")

    val grafoQualquer = Grafo(vertices, arestas)

    println(grafoQualquer)
}