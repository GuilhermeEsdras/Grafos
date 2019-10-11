from Roteiro6.Roteiro6__funcoes import Grafo
import copy

grafo_direcionado = Grafo()
for v in ['A', 'B', 'C', 'D']:
    grafo_direcionado.adicionaVertice(v)
for a in ['A-C', 'C-D', 'D-B', 'B-C', 'C-B']:
    grafo_direcionado.adicionaAresta(a)
print(grafo_direcionado)

n = copy.deepcopy(grafo_direcionado.N)
m = grafo_direcionado.warshall()
grafo_warshall = Grafo(n, m)
print(grafo_warshall)
