from grafo import Grafo
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
print('grafo_ex {} um caminho entre E e I'.format(
    'possui' if grafo_ex.caminho_dois_vertices('E', 'I') else 'não possui'))
print('grafo_ex {} conexo'.format('é' if grafo_ex.conexo() else 'não é'))

##

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
print('grafo_conexo {} conexo'.format('é' if grafo_conexo.conexo() else 'não é'))
print('grafo_desconexo {} conexo'.format('é' if grafo_desconexo.conexo() else 'não é'))
