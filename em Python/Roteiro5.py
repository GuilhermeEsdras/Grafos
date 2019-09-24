from Roteiro5_4__grafo_adj_nao_dir import Grafo

# # Pontes de Königsberg
# konigsberg = Grafo()
# for v in ['M', 'T', 'B', 'R']:
#     konigsberg.adicionaVertice(v)
# for a in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
#     konigsberg.adicionaAresta(a)
# # print(konigsberg)
#
# # Grafo da Paraíba
# paraiba = Grafo()
# for v in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
#     paraiba.adicionaVertice(v)
# for a in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
#     paraiba.adicionaAresta(a)
# print(paraiba)
# print(paraiba.eh_uma_ponte('C-E'))
#
# # Grafo do Exemplo
# ex_graph = Grafo()
# for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
#     ex_graph.adicionaVertice(v)
# for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-B', 'B-D', 'B-F', 'F-H', 'H-G', 'G-I', 'I-J', 'J-K', 'J-A', 'J-G', 'K-G',
#           'A-G', 'B-G', 'L-L']:
#     ex_graph.adicionaAresta(a)
# print(ex_graph)
# print(ex_graph.caminho_dois_vertices('B', 'B'))
# print(ex_graph.ah_ciclo())
# print(ex_graph.eh_conexo())
# print(ex_graph.eh_euleriano())
#
# print()
# Grafo Euleriano
euleriano = Grafo()
for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    euleriano.adicionaVertice(v)
for a in ['A-B', 'A-F', 'B-C', 'B-G', 'B-F', 'F-E', 'F-G', 'G-C', 'G-E', 'E-C',
          'E-D', 'D-C']:
    euleriano.adicionaAresta(a)
print(euleriano)
# print(euleriano.eh_euleriano())
# print(euleriano.caminho_euleriano())

lista_1 = ['A-B', 'B-C', 'C-D', 'D-E', 'E-C', 'C-G', 'G-B', 'B-F', 'F-E', 'E-G', 'G-F', 'F-A']
lista_2 = ['A-B', 'A-F', 'B-C', 'B-F', 'B-G', 'C-D', 'C-E', 'C-G', 'D-E', 'E-F', 'E-G', 'F-G']
cont = 0
for pos, aresta in enumerate(lista_1):
    aresta_reverse = aresta[::-1]
    if aresta in lista_2 or aresta_reverse in lista_2:
        cont += 1