from Roteiro5.Roteiro5__grafos import Grafos


def printaGrafoComNome(nome, grafo):
    print("{} \n|{}|".format("-" * (len(nome) + 2), nome))
    print(grafo)


def printaPerguntaComResposta(pergunta, resposta):
    print("{}".format(pergunta))
    print("R: ", resposta)


print()  # ----------------------- #

simples = Grafos.euleriano_bem_simples
printaGrafoComNome("Bem Simples", simples)
# simples.grafoParaPNG("simples")
printaPerguntaComResposta("Possui Caminho Euleriano?", simples.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", simples.ciclo_hamiltoniano())

semi_euler = Grafos.semi_euler
printaGrafoComNome("Semi-Euleriano 1", semi_euler)
# semi_euler.grafoParaPNG("semi_euler")
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", semi_euler.ciclo_hamiltoniano())

semi_euler_2 = Grafos.semi_euler_2
printaGrafoComNome("Semi-Euleriano 2", semi_euler_2)
# semi_euler_2.grafoParaPNG("semi_euler_2")
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_2.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", semi_euler_2.ciclo_hamiltoniano())

semi_euler_3 = Grafos.semi_euler_3
printaGrafoComNome("Semi-Euleriano 3", semi_euler_3)
# semi_euler_3.grafoParaPNG("semi_euler_3")
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_3.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", semi_euler_3.ciclo_hamiltoniano())

semi_euler_laco = Grafos.semi_euler_com_laco
printaGrafoComNome("Semi-Euleriano Com Laço", semi_euler_laco)
# semi_euler_laco.grafoParaPNG("semi_euler_laco")
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_laco.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", semi_euler_laco.ciclo_hamiltoniano())

print()  # ----------------------- #

# |Pontes de Konigsberg|
konigsberg = Grafos.konigsberg
printaGrafoComNome("Pontes de Konigsberg", konigsberg)
# konigsberg.grafoParaPNG("konigsberg")
printaPerguntaComResposta("Possui Caminho Euleriano?", konigsberg.caminho_euleriano())

print()  # ----------------------- #

# |Pontes de Konigsberg (Modificado)|
konigsberg_mod = Grafos.konigsberg_mod
printaGrafoComNome("Pontes de Konigsberg (Modificado)", konigsberg_mod)
# konigsberg_mod.grafoParaPNG("konigsberg_mod")
printaPerguntaComResposta("Possui Caminho Euleriano?", konigsberg_mod.caminho_euleriano())

print()  # ----------------------- #

# |Grafo da Paraíba|
paraiba = Grafos.paraiba
printaGrafoComNome("Grafo da Paraíba", paraiba)
# paraiba.grafoParaPNG("paraiba")
printaPerguntaComResposta("Possui Caminho Euleriano?", paraiba.caminho_euleriano())

print()  # ----------------------- #

# |Grafo da Paraíba Modificado|
pb_mod = Grafos.paraiba_euler
printaGrafoComNome("Grafo da Paraíba Modificado", pb_mod)
# pb_mod.grafoParaPNG("paraiba_mod")
printaPerguntaComResposta("Possui Caminho Euleriano?", pb_mod.caminho_euleriano())

print()  # ----------------------- #

euleriano_hamiltoniano = Grafos.euleriano
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", euleriano_hamiltoniano.ciclo_hamiltoniano())
