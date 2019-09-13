from Roteiro5__grafo_adj_nao_dir import Grafo

# Pontes de Konigsberg
konigsberg = Grafo([], [])
for i in ['M', 'T', 'B', 'R']:
    konigsberg.adiciona_vertice(i)
for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
    konigsberg.adiciona_aresta(i)

print(konigsberg)
