from grafo_adj_nao_dir import Grafo

#Primeira questao
g = Grafo(['J', 'C', 'E', 'P'])
g.adicionaAresta('J-C')
g.adicionaAresta('C-E')
g.adicionaAresta('E-P')
g.adicionaAresta('J-P')
g.adicionaAresta("E-C")

print(g.eh_conexo())

