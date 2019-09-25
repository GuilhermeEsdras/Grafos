from Roteiro5_4__grafo_adj_nao_dir import Grafo

# # Pontes de Königsberg
# konigsberg = Grafo()
# for v in ['M', 'T', 'B', 'R']:
#     konigsberg.adicionaVertice(v)
# for a in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
#     konigsberg.adicionaAresta(a)
# # print(konigsberg)

# # Grafo da Paraíba
# paraiba = Grafo()
# for v in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
#     paraiba.adicionaVertice(v)
# for a in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
#     paraiba.adicionaAresta(a)
# print(paraiba)
# # print(paraiba.eh_uma_ponte('C-E'))
# print(paraiba.caminho_euleriano())


# Grafo do Exemplo
ex_graph = Grafo()
for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
    ex_graph.adicionaVertice(v)
for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-B', 'B-D', 'B-F', 'F-H', 'H-G', 'G-I', 'I-J', 'J-K', 'J-A', 'J-G', 'K-G',
          'A-G', 'B-G']:
    ex_graph.adicionaAresta(a)
print(ex_graph)
print(ex_graph.caminho_dois_vertices('B', 'B'))
print(ex_graph.ah_ciclo())
print(ex_graph.eh_conexo())
print(ex_graph.eh_euleriano())
print(ex_graph.caminho_euleriano())

# # Grafo Euleriano
# euleriano = Grafo()
# for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
#     euleriano.adicionaVertice(v)
# for a in ['A-B', 'A-F', 'B-C', 'B-G', 'B-F', 'F-E', 'F-G', 'G-C', 'G-E', 'E-C',
#           'E-D', 'D-C']:
#     euleriano.adicionaAresta(a)
# print(euleriano)
# # print(euleriano.eh_euleriano())
# print(euleriano.caminho_euleriano())
