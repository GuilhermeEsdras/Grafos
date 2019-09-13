from grafo_adj_nao_dir import Grafo

k3 = Grafo(['A', 'B', 'C'])
k3.adicionaAresta('A-B')
k3.adicionaAresta('B-C')
k3.adicionaAresta('C-A')
# print(k3)

paraiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
paraiba.adicionaAresta('J-C')
paraiba.adicionaAresta('C-E')
paraiba.adicionaAresta('C-E')
paraiba.adicionaAresta('C-P')
paraiba.adicionaAresta('C-P')
paraiba.adicionaAresta('C-M')
paraiba.adicionaAresta('C-T')
paraiba.adicionaAresta('M-T')
paraiba.adicionaAresta('T-Z')
print(paraiba)
print(paraiba.arestas_sobre_vertice('C'))
