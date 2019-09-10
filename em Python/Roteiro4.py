from grafo_adj_nao_dir import Grafo

k3 = Grafo(['A', 'B', 'C'])
k3.adicionaAresta('A-B')
k3.adicionaAresta('B-C')
k3.adicionaAresta('C-A')
print(k3)
