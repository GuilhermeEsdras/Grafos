import random
from grafo_adj_nao_dir import Grafo

# k3 = Grafo(['A', 'B', 'C'])
# for aresta in ['A-B', 'B-C', 'C-A']:
# print(k3)

##
print('Grafo da Paraíba:')

paraiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
for aresta in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
    paraiba.adicionaAresta(aresta)
print(paraiba)

vertice_aleatorio = random.choice(paraiba.N)
print('vertices_nao_adjacentes:', paraiba.vertices_nao_adjacentes())
print('ha_laco?', paraiba.ha_laco())
print('grau de {}:'.format(vertice_aleatorio), paraiba.grau(vertice_aleatorio))
print('ha_paralelas?', paraiba.ha_paralelas())
print('arestas_sobre_vertice {}:'.format(vertice_aleatorio), paraiba.arestas_sobre_vertice(vertice_aleatorio))
print('eh_completo?', paraiba.eh_completo(), '\n')

##
print('Grafo completo:')

grafo_completo = Grafo(['J', 'C', 'E', 'P'])
for aresta in ['J-C', 'J-P', 'J-E', 'C-E', 'C-P', 'P-E']:
    grafo_completo.adicionaAresta(aresta)
print(grafo_completo)

print('eh_completo?', grafo_completo.eh_completo())
