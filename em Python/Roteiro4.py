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
print(paraiba.eh_completo())

grafo_completo = Grafo(
    ['J', 'C', 'E', 'P']
)
grafo_completo.adicionaAresta('J-C')
grafo_completo.adicionaAresta('J-P')
grafo_completo.adicionaAresta('J-E')
grafo_completo.adicionaAresta('C-E')
grafo_completo.adicionaAresta('C-P')
grafo_completo.adicionaAresta('P-E')
print(grafo_completo)
print(grafo_completo.eh_completo())
