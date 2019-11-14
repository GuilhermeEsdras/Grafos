from Roteiro7.Roteiro7__funcoes import GrafoComPesos

grafo_aula = GrafoComPesos(
    ['E', 'A', 'B', 'C', 'D'],
    {
        'E-A': 1,
        'E-C': 10,
        'A-B': 2,
        'B-C': 4,
        'C-D': 3
    }
)
print(grafo_aula)
print('Menor caminho por Dijkstra: ', grafo_aula.dijkstra('E', 'D'))

print("-------------------------")

grafo_aula2 = GrafoComPesos(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    {
        'A-B': 1, 'A-F': 3, 'A-G': 2,
        'B-F': 1,
        'C-B': 2,
        'C-D': 5,
        'D-E': 2,
        'F-D': 4,
        'F-G': 2,
        'G-E': 7,
    }
)
print(grafo_aula2)
print('Menor caminho por Dijkstra: ', grafo_aula2.dijkstra('A', 'E'))
