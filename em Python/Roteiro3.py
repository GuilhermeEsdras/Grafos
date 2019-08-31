from grafo import Grafo

PB_vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
PB_arestas = {
    'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E',
    'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M',
    'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'
}
paraiba = Grafo(PB_vertices, PB_arestas)
print(paraiba.encontraCaminho(4))

###

ex_vertices = ['A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J',
               'K']
ex_arestas = {
    '1': 'A-B', '2': 'A-G', '3': 'A-J', '4': 'G-K',
    '5': 'K-J', '6': 'J-G', '7': 'J-I', '8': 'I-G',
    '9': 'G-H', '10': 'H-F', '11': 'F-B', '12': 'G-B',
    '13': 'B-C', '14': 'C-D', '15': 'E-D', '16': 'B-D',
    '17': 'B-E'
}
grafo_ex = Grafo(ex_vertices, ex_arestas)
print(grafo_ex.encontraCaminho(4))
