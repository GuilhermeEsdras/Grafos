from Roteiro8.Roteiro8__funcoes import Grafo

grafo = Grafo()
for vertice in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    grafo.adicionaVertice(vertice)
grafo.adicionaArestaComPeso('A-D', 5)
grafo.adicionaArestaComPeso('A-B', 7)
grafo.adicionaArestaComPeso('B-C', 8)
grafo.adicionaArestaComPeso('B-E', 7)
grafo.adicionaArestaComPeso('C-E', 5)
grafo.adicionaArestaComPeso('D-B', 9)
grafo.adicionaArestaComPeso('D-E', 15)
grafo.adicionaArestaComPeso('D-F', 6)
grafo.adicionaArestaComPeso('E-F', 8)
grafo.adicionaArestaComPeso('E-G', 9)
grafo.adicionaArestaComPeso('F-G', 11)

print(grafo)
print(grafo.kruskal())
