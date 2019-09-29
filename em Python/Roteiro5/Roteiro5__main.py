from Roteiro5.Roteiro5__grafos import Grafos


def printaGrafoComNome(nome, grafo):
    print("{} \n|{}|".format("-" * (len(nome) + 2), nome))
    print(grafo)


def printaPerguntaComResposta(pergunta, resposta):
    print("{}".format(pergunta))
    print("R: ", resposta)


print()  # ----------------------- #

# --- | Grafos Semi-Eulerianos | --- #

simples = Grafos.euleriano_bem_simples
printaGrafoComNome("|Bem Simples", simples)
printaPerguntaComResposta("Possui Caminho Euleriano?", simples.caminho_euleriano())

semi_euler = Grafos.semi_euler
printaGrafoComNome("Semi-Euleriano 1", semi_euler)
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler.caminho_euleriano())

semi_euler_2 = Grafos.semi_euler_2
printaGrafoComNome("Semi-Euleriano 2", semi_euler_2)
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_2.caminho_euleriano())

semi_euler_3 = Grafos.semi_euler_3
printaGrafoComNome("Semi-Euleriano 3", semi_euler_3)
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_3.caminho_euleriano())

semi_euler_laco = Grafos.semi_euler_com_laco
printaGrafoComNome("Semi-Euleriano Com Laço", semi_euler_laco)
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_laco.caminho_euleriano())

print()  # ----------------------- #

# --- | Grafos Hamiltonianos | --- #



print()  # ----------------------- #

# |Pontes de Konigsberg|
konigsberg = Grafos.konigsberg
printaGrafoComNome("Pontes de Konigsberg", konigsberg)
printaPerguntaComResposta("Possui Caminho Euleriano?", konigsberg.caminho_euleriano())

print()  # ----------------------- #

# |Pontes de Konigsberg (Modificado)|
konigsberg_mod = Grafos.konigsberg_mod
printaGrafoComNome("Pontes de Konigsberg (Modificado)", konigsberg_mod)
printaPerguntaComResposta("Possui Caminho Euleriano?", konigsberg_mod.caminho_euleriano())

print()  # ----------------------- #

# |Grafo da Paraíba|
paraiba = Grafos.paraiba
printaGrafoComNome("Grafo da Paraíba", paraiba)
printaPerguntaComResposta("Possui Caminho Euleriano?", paraiba.caminho_euleriano())

print()  # ----------------------- #

# |Grafo da Paraíba Modificado|
pb_mod = Grafos.paraiba_euler
printaGrafoComNome("Grafo da Paraíba Modificado", pb_mod)
printaPerguntaComResposta("Possui Caminho Euleriano?", pb_mod.caminho_euleriano())

print()  # ----------------------- #


