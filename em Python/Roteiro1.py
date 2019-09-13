from Roteiro3_2_1__grafo import Grafo

paraiba = Grafo()
paraiba.adicionaVertice('V')
paraiba.adicionaVertice('J')
paraiba.adicionaVertice('C')
paraiba.adicionaVertice('E')
paraiba.adicionaVertice('P')
paraiba.adicionaVertice('M')
paraiba.adicionaVertice('T')
paraiba.adicionaVertice('Z')
paraiba.adicionaAresta('a1', 'J-C')
paraiba.adicionaAresta('a2', 'C-E')
paraiba.adicionaAresta('a3', 'C-E')
paraiba.adicionaAresta('a4', 'C-P')
paraiba.adicionaAresta('a5', 'C-P')
paraiba.adicionaAresta('a6', 'C-M')
paraiba.adicionaAresta('a7', 'C-T')
paraiba.adicionaAresta('a8', 'M-T')
paraiba.adicionaAresta('a9', 'T-Z')

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
print('2 - c) Há grafo paralelas? - {}'.format('Sim' if paraiba.ha_paralelas() else 'Não'))

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
