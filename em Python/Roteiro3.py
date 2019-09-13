from Roteiro3_2_1__grafo import Grafo
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
v1, v2 = 'E', 'F'
print('grafo_ex {} um caminho entre '.format('possui' if grafo_ex.caminho_dois_vertices(v1, v2) else 'não possui')
      + v1 + ' e ' + v2)
print(grafo_ex.caminho_dois_vertices(v1, v2))
print('grafo_ex {} conexo'.format('é' if grafo_ex.conexo() else 'não é'))
print(grafo_ex.caminho(6))
print(grafo_ex.caminho(7))
print(grafo_ex.caminho(8))
print(grafo_ex.caminho(9))
print('grafo_ex.ha_ciclo():', grafo_ex.ha_ciclo())

###

grafo_conexo = Grafo([
    '1', '2', '3', '5', '6', '7'
], {
    'a1': '1-2', 'a2': '2-3', 'a3': '1-5',
    'a4': '2-6', 'a5': '3-7'
})
grafo_desconexo = Grafo([
    '1', '2', '3', '5', '6', '7'
], {
    'a1': '1-2', 'a2': '2-3', 'a3': '1-5',
    'a4': '3-7'
})
print('grafo_desconexo.ha_ciclo():', grafo_desconexo.ha_ciclo())
print('grafo_conexo {} conexo'.format('é' if grafo_conexo.conexo() else 'não é'))
print('grafo_desconexo {} conexo'.format('é' if grafo_desconexo.conexo() else 'não é'))
print(grafo_conexo.caminho(2))

###

paraiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {
    'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E',
    'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M',
    'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'
})
print('paraiba.ha_ciclo(): ', paraiba.ha_ciclo())
paraiba_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {
    'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P',
    'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T',
    'a9': 'T-Z'})
print('paraiba_sem_paralelas.ha_ciclo()', paraiba_sem_paralelas.ha_ciclo())
