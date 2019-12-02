from Roteiro8.Roteiro8__funcoes import Grafo

grafo_wiki = Grafo()
for vertice in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    grafo_wiki.adicionaVertice(vertice)
grafo_wiki.adicionaArestaComPeso('A-D', 5)
grafo_wiki.adicionaArestaComPeso('A-B', 7)
grafo_wiki.adicionaArestaComPeso('B-C', 8)
grafo_wiki.adicionaArestaComPeso('B-E', 7)
grafo_wiki.adicionaArestaComPeso('C-E', 5)
grafo_wiki.adicionaArestaComPeso('D-B', 9)
grafo_wiki.adicionaArestaComPeso('D-E', 15)
grafo_wiki.adicionaArestaComPeso('D-F', 6)
grafo_wiki.adicionaArestaComPeso('E-F', 8)
grafo_wiki.adicionaArestaComPeso('E-G', 9)
grafo_wiki.adicionaArestaComPeso('F-G', 11)

print(grafo_wiki)
print(grafo_wiki.alpha('E-C'))

