from Roteiro1.Roteiro1__grafos import GrafosProntos

paraiba = GrafosProntos.paraiba

print("GrafoComPesos da Paraíba:")
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
print('2 - c) Há grafo paralelas? - {}'.format('Sim' if paraiba.ha_paralelas() else 'Não'))

print()
# Teste 2-v2)
for vertice in paraiba.N:
    print('2 - v2) Grau do vértice {}: {}'.format(vertice, paraiba.grau('{}'.format(vertice))))

print()
# Teste 2-e)
v = 'C'
print('2 - e) Lista de vértices que incidem sobre o vértice {} da Paraíba: \n'.format(v),
      paraiba.arestas_sobre_vertice('{}'.format(v)))

print()
# Teste 2-f)
print('2 - f) Eh completo? {}'.format('Sim' if paraiba.eh_completo() else 'Não'))
