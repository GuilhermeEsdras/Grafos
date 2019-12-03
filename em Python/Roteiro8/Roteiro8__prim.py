from Roteiro8.Roteiro8__funcoes import Grafo

grafo = Grafo()
for v in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    grafo.adicionaVertice(v)
for a, p in {'a-b': 9, 'a-g': 4,
             'b-c': 6, 'b-g': 10, 'b-h': 7,
             'c-d': 8, 'c-e': 12, 'c-f': 8,
             'd-e': 14,
             'e-f': 2,
             'f-h': 2, 'f-g': 1}.items():
    grafo.adicionaArestaComPeso(a, p)

print('Grafo:')
print(grafo)
print('Pesos:', grafo.pesos())

print()

print('Minimum Spanning Tree com Prim Modificado:')
print(grafo.prim_mod())
