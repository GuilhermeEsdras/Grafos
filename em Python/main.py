from grafo import Grafo
from grafo_test import TestGrafo

vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
arestas = {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T',
                 'a8': 'M-T', 'a9': 'T-Z'}

paraiba = Grafo(vertices, arestas)

print("Grafo da Paraíba:")
print('Vértices (N): ', paraiba.N)
print('Arestas (An): ', paraiba.A)
print()

# Teste 2-a)
print('2 - a) Pares de Vértices não adjacentes:')
for i, aresta in enumerate(paraiba.vertices_nao_adjacentes()):
    if (i+1) % 10 == 0:
        print('{}, '.format(aresta) if i != (len(paraiba.vertices_nao_adjacentes()) - 1) else
              '{}.\n'.format(aresta))
    else:
        print('{}, '.format(aresta) if i != (len(paraiba.vertices_nao_adjacentes()) - 1) else
              '{}.\n'.format(aresta), end='')

print()
# Teste 2-b)
print('2 - b) Há Vértices Adjacentes a ele mesmo/Laços? - {}'.format('Sim' if paraiba.ha_laco() else 'Não'))

print()
# Teste 2-c)
print('2 - c) Há arestas paralelas? - {}'.format('Sim' if paraiba.ha_paralelas() else 'Não'))

print()
# Teste 2-d)
for vertice in paraiba.N:
    print('2 - d) Grau do vértice {}: {}'.format(vertice, paraiba.grau('{}'.format(vertice))))

print()
# Teste 2-e)
v = 'C'
print('2 - e) Lista de vértices que incidem sobre o vértice {} da Paraíba: \n'.format(v),
      paraiba.arestas_sobre_vertice('{}'.format(v)))

print()
# Teste 2-f)
print('2 - f) Eh completo? {}'.format('Sim' if paraiba.eh_completo() else 'Não'))
