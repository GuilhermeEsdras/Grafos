from Roteiro7.Roteiro7__funcoes import GrafoComPesos


# Arquivo de Testes da classe "GrafoComPesos" #
# --------------------------------------------------------------------------- #
teste_basico = GrafoComPesos(
    ['A', 'B', 'C', 'D', 'E'],
    {
        'A-B': 2,
        'B-C': 5,
        'E-D': 8,
        'C-E': 3
    }
)
print("Matriz com pesos")
print(teste_basico)
print("Matriz sem pesos")
print(teste_basico.matriz_sem_pesos())

print("-----")

testando = GrafoComPesos()
testando.adicionaVertice('A')
testando.adicionaVertice('B')
testando.adicionaVertice('CC')
testando.adicionaVertice('D')
testando.adicionaVertice('EEEEEE')
testando.adicionaAresta('A-B', 2)
testando.adicionaAresta('CC-A', 1)
print("Matriz com pesos")
print(testando)
print("Matriz sem pesos")
print(testando.matriz_sem_pesos())

print("-----")

print("Peso da aresta \'A-B\' modificado para 1")
testando.modifica_peso('A-B', 1)
print(testando)

print("-----")

testando_com_dict = GrafoComPesos(
    ['A', 'BBB', 'CC', 'D', 'EE'],  # <- Lista com os Vértices
    {  # Dicionário com as Arestas e seus Pesos:
        'A-BBB': 2,
        'CC-A': 1
    }
)
print("Matriz com pesos")
print(testando_com_dict)
print("Matriz sem pesos")
print(testando_com_dict.matriz_sem_pesos())

