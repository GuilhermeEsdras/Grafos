import random
from Roteiro4.Roteiro4__grafos import Grafos

k3 = Grafos.k3
print(k3)

###

print('GrafoComPesos da Paraíba:')
paraiba = Grafos.paraiba
print(paraiba)

vertice_aleatorio = random.choice(paraiba.N)
print('vertices_nao_adjacentes:', paraiba.vertices_nao_adjacentes())
print('ha_laco?', paraiba.ha_laco())
print('grau de {}:'.format(vertice_aleatorio), paraiba.grau(vertice_aleatorio))
print('ha_paralelas?', paraiba.ha_paralelas())
print('arestas_sobre_vertice {}:'.format(vertice_aleatorio), paraiba.arestas_sobre_vertice(vertice_aleatorio))
print('eh_completo?', paraiba.eh_completo(), '\n')

###

print('GrafoComPesos completo:')

grafo_completo = Grafos.grafo_completo
print(grafo_completo)

print('eh_completo?', grafo_completo.eh_completo())
