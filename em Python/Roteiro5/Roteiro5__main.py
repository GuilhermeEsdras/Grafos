from Roteiro5.Roteiro5__grafos import Grafos
from Roteiro5.Roteiro5__funcoes import Grafo
import time


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
# printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", simples.ciclo_hamiltoniano())

time.sleep(0.5)

semi_euler = Grafos.semi_euler
printaGrafoComNome("Semi-Euleriano 1", semi_euler)
# semi_euler.grafoParaPNG("semi_euler")
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", semi_euler.ciclo_hamiltoniano())

time.sleep(0.5)

semi_euler_2 = Grafos.semi_euler_2
printaGrafoComNome("Semi-Euleriano 2", semi_euler_2)
# semi_euler_2.grafoParaPNG("semi_euler_2")
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_2.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", semi_euler_2.ciclo_hamiltoniano())

time.sleep(0.5)

semi_euler_3 = Grafos.semi_euler_3
printaGrafoComNome("Semi-Euleriano 3", semi_euler_3)
# semi_euler_3.grafoParaPNG("semi_euler_3")
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_3.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", semi_euler_3.ciclo_hamiltoniano())

time.sleep(0.5)

semi_euler_laco = Grafos.semi_euler_com_laco
printaGrafoComNome("Semi-Euleriano Com Laço", semi_euler_laco)
# semi_euler_laco.grafoParaPNG("semi_euler_laco")
printaPerguntaComResposta("Possui Caminho Euleriano?", semi_euler_laco.caminho_euleriano())
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", semi_euler_laco.ciclo_hamiltoniano())

print()  # ----------------------- #

time.sleep(0.5)

# |Pontes de Konigsberg|
konigsberg = Grafos.konigsberg
printaGrafoComNome("Pontes de Konigsberg", konigsberg)
# konigsberg.grafoParaPNG("konigsberg")
printaPerguntaComResposta("Possui Caminho Euleriano?", konigsberg.caminho_euleriano())

print()  # ----------------------- #

time.sleep(0.5)

# |Pontes de Konigsberg (Modificado)|
konigsberg_mod = Grafos.konigsberg_mod
printaGrafoComNome("Pontes de Konigsberg (Modificado)", konigsberg_mod)
# konigsberg_mod.grafoParaPNG("konigsberg_mod")
printaPerguntaComResposta("Possui Caminho Euleriano?", konigsberg_mod.caminho_euleriano())

print()  # ----------------------- #

time.sleep(0.5)

# |Grafo da Paraíba|
paraiba = Grafos.paraiba
printaGrafoComNome("Grafo da Paraíba", paraiba)
# paraiba.grafoParaPNG("paraiba")
printaPerguntaComResposta("Possui Caminho Euleriano?", paraiba.caminho_euleriano())

print()  # ----------------------- #

time.sleep(0.5)

# |Grafo da Paraíba Modificado|
pb_mod = Grafos.paraiba_euler
printaGrafoComNome("Grafo da Paraíba Modificado", pb_mod)
# pb_mod.grafoParaPNG("paraiba_mod")
printaPerguntaComResposta("Possui Caminho Euleriano?", pb_mod.caminho_euleriano())

print()  # ----------------------- #

time.sleep(0.5)

# |Testes de Ciclo Hamiltoniano|
com_ciclo_hamiltoniano = Grafos.com_ciclo_hamiltoniano
printaGrafoComNome("Grafo com Ciclo Hamiltoniano", com_ciclo_hamiltoniano)
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", com_ciclo_hamiltoniano.ciclo_hamiltoniano())

time.sleep(0.5)

euleriano_hamiltoniano = Grafos.euleriano
printaGrafoComNome("Outro Grafo com Ciclo Hamiltoniano", euleriano_hamiltoniano)
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", euleriano_hamiltoniano.ciclo_hamiltoniano())

time.sleep(0.5)


euleriano_nao_hamiltoniano = Grafos.euleriano_2
printaGrafoComNome("Grafo Euleriano Sem Ciclo Hamiltoniano", euleriano_nao_hamiltoniano)
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", euleriano_nao_hamiltoniano.ciclo_hamiltoniano())

time.sleep(0.5)

nao_hamiltoniano = Grafo()
for v in ['1', '2', '3', '4', '5', '6', '7']:
    nao_hamiltoniano.adicionaVertice(v)
for a in ['1-2', '2-3', '3-4', '4-5', '5-3', '3-6', '6-7', '7-3']:
    nao_hamiltoniano.adicionaAresta(a)

printaGrafoComNome("semi_euler_3", nao_hamiltoniano)
printaPerguntaComResposta("Possui Ciclo Hamiltoniano?", nao_hamiltoniano.ciclo_hamiltoniano())
