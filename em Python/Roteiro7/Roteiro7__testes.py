from Roteiro7.Roteiro7__funcoes import GrafoComPesos

testando = GrafoComPesos()
testando.adicionaVertice('A')
testando.adicionaVertice('B')
testando.adicionaVertice('CC')
testando.adicionaVertice('D')
testando.adicionaVertice('EEEEEE')
testando.adicionaAresta('A-B', 2)
testando.adicionaAresta('CC-A', 1)
print(testando)


testando_com_dict = GrafoComPesos(
    ['A', 'B', 'CC', 'D', 'EEEEEE'],  # <- Lista com os Vértices
    {  # Dicionário com as Arestas e seus Pesos:
        'A-B': 2,
        'CC-A': 1
    }
)
print(testando_com_dict)


testando.modifica_peso('A-B', 1)
print(testando)
