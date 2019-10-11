from Roteiro6.Roteiro6__funcoes import Grafo

grafo_direcionado = Grafo()
for v in ['A', 'B', 'C', 'D']:
    grafo_direcionado.adicionaVertice(v)
for a in ['A-C', 'C-D', 'D-B', 'B-C', 'C-B']:
    grafo_direcionado.adicionaAresta(a)
print(grafo_direcionado)
print(grafo_direcionado.grafo_warshall())

print("---")

grafo_aula = Grafo()
for v in ['1', '2', '3', '4']:
    grafo_aula.adicionaVertice(v)
for a in ['1-2', '2-4', '4-2', '4-3']:
    grafo_aula.adicionaAresta(a)
print(grafo_aula)
print(grafo_aula.grafo_warshall())
