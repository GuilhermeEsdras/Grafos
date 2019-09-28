from Roteiro3.Roteiro3__grafos import Grafos


grafo_ex = Grafos.grafo_ex
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

grafo_conexo = Grafos.grafo_conexo
grafo_desconexo = Grafos.grafo_desconexo
print('grafo_desconexo.ha_ciclo():', grafo_desconexo.ha_ciclo())
print('grafo_conexo {} conexo'.format('é' if grafo_conexo.conexo() else 'não é'))
print('grafo_desconexo {} conexo'.format('é' if grafo_desconexo.conexo() else 'não é'))
print(grafo_conexo.caminho(2))

###

paraiba = Grafos.paraiba
print('paraiba.ha_ciclo(): ', paraiba.ha_ciclo())

paraiba_sem_paralelas = Grafos.paraiba_sem_paralelas
print('paraiba_sem_paralelas.ha_ciclo()', paraiba_sem_paralelas.ha_ciclo())
