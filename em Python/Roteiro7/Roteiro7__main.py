from Roteiro7.Roteiro7__funcoes import GrafoComPesos
from Roteiro7.Roteiro7__exceptions import *


# .:: Arquivo que coloca em prática as funções referentes ao Roteiro 7 ::. #
# --------------------------------------------------------------------------- #
# Funções Auxiliares:
def executa(mapa, tipo_dijkstra):
    # ----
    print("|Matriz de Adjacência do Mapa|")
    # -
    print(mapa.matriz_sem_pesos())
    print("---")

    # ----
    print("|Atributos adicionais do Mapa|\n---")
    # -
    while True:
        u = input("> Digite o Ponto de Partida (u): ")
        if not mapa.existeVertice(u):
            print("> O vértice \"{}\" não existe no mapa! Tente novamente...".format(u))
        else:
            break
    # -
    while True:
        v = input("> Digite o Ponto de Destino (v): ")
        if not mapa.existeVertice(v):
            print("> O vértice \"{}\" não existe no mapa! Tente novamente...".format(v))
        else:
            break
    print("---")

    # ----
    if tipo_dijkstra == 1:
        caminho_mapa = mapa.dijkstra(u, v)
        if caminho_mapa:
            print('> Menor caminho entre {} e {} no Mapa usando Dijkstra: '.format(u, v), caminho_mapa)
        else:
            print("> Não foi possível encontrar um caminho de {} a {} "
                  "para este Mapa usando Dijkstra! :(".format(u, v))
        print("---")

    # ----
    elif qual_dijkstra == 2:
        # ----
        quantidade = int(input("> Digite a quantidade de Pontos de Recarga: "))
        # -
        pontos_de_recarga = []
        for x in range(quantidade):
            while True:
                vertice = input("> Digite o Ponto de Recarga nº {} (ou \"sair\" quando terminar): ".format(x))
                if vertice != "sair":
                    if not mapa.existeVertice(vertice):
                        print("> O vértice \"{}\" não existe no mapa! Tente novamente...".format(vertice))
                    else:
                        pontos_de_recarga[x] = vertice
                        break
                else:
                    break
            if vertice == "sair":
                break
        print("---")

        # ----
        print("|Atributos do Drone|\n---")
        # -
        carga_maxima = int(input("> Digite a Capacidade Máxima de Carga do Drone: "))
        # -
        carga_inicial = int(input("> Digite Carga Inicial: "))
        print("---")

        # ----
        dados_iniciais(carga_maxima, carga_inicial, u, v, pontos_de_recarga)

        # ----
        melhor__caminho = mapa.dijkstra_mod(u, v, carga_inicial, carga_maxima, pontos_de_recarga)
        if melhor__caminho:
            melhor_caminho(u, v)
            print('>', melhor__caminho)
        else:
            print("> Não foi possível encontrar um caminho com os dados informados! :(")

    print(separador())


def dados_iniciais(c_m, c_i, p_i, p_f, p_de_r):
    print("|Dados Iniciais|\n---"
          "\n• Carga Máxima:", c_m,
          "\n• Carga Inicial:", c_i,
          "\n• Ponto Inicial:", p_i,
          "\n• Ponto Final:", p_f,
          "\n• Pontos de Recarga:", p_de_r)
    print("---")


def melhor_caminho(c_i, c_m):
    print('> Melhor caminho neste Mapa para o Drone com Carga Inicial {}: '.format('de {}'.format(c_i))
          if c_i < c_m else '{} ({})'.format('Máxima', c_m))


def sair():
    print("Saindo...")
    exit(0)


def separador():
    return "------------------------"


# --------------------------------------------------------------------------- #
mapa_pronto = GrafoComPesos(
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
     '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
     '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
     '31', '32', '33'],
    {
        '1-2': 1, '1-3': 1, '1-4': 1,
        '2-5': 1, '2-9': 1,
        '3-7': 1,
        '4-3': 1, '4-8': 1,
        '5-6': 1,
        '6-2': 1, '6-10': 1,
        '7-6': 1, '7-10': 1, '7-11': 1,
        '8-7': 1, '8-12': 1,
        '9-13': 1,
        '10-9': 1, '10-14': 1,
        '11-15': 1,
        '12-16': 1,
        '13-17': 1, '13-19': 1,
        '14-18': 1, '14-19': 1, '14-20': 1,
        '15-19': 1,
        '16-20': 1,
        '17-21': 1,
        '18-17': 1, '18-22': 1,
        '19-18': 1, '19-24': 1,
        '20-19': 1,
        '21-29': 1, '21-25': 1,
        '22-25': 1, '22-26': 1, '22-23': 1,
        '23-19': 1,
        '24-27': 1, '24-28': 1,
        '27-31': 1,
        '29-30': 1,
        '30-31': 1,
        '31-32': 1, '31-33': 1,
        '33-32': 1
    }
)
# --------------------------------------------------------------------------- #
# Variável auxiliar:
testando = False  # TODO: Alterar para "True" se não estiver testando!!!

# --------------------------------------------------------------------------- #
# Main #

while True:
    dados = 0
    qual_dijkstra = 0
    qual_mapa = 0
    if not testando:
        while True:
            op = int(input(
                "> Qual mapa/grafo deseja utilizar?"
                "\n\t 1- Mapa pronto do Roteiro 7"
                "\n\t 2- Criar um novo mapa"
                "\n\t 3- Sair"
                "\n\t\t Digite a opção: ")
            )
            if op == 1 or op == 2:
                qual_mapa = op
                break
            elif op == 3:
                sair()
            else:
                print("Opção inválida! Tente novamente...")
        # -
        print(separador())
        # -
        while True:
            op = int(input(
                "> Qual algoritmo desejar utilizar nesse mapa?"
                "\n\t 1- Dijkstra Comum (Menor caminho entre u e v)"
                "\n\t 2- Dijkstra Modificado para um Drone (Melhor caminho considerando bateria e pontos de recarga)"
                "\n\t 3- Sair"
                "\n\t\t Digite a opção: ")
            )
            if op == 1 or op == 2:
                qual_dijkstra = op
                break
            elif op == 3:
                sair()
            else:
                print("Opção inválida! Tente novamente...")
        # -
        print(separador())
        # -
        if qual_mapa == 1:
            while True:
                op = int(input(
                    "> E o que deseja fazer em relação aos dados desse mapa (u, v, carga inicial, carga máxima, etc)?"
                    "\n\t 1- Utilizar os dados prontos do arquivo"
                    "\n\t 2- Inserir novos dados"
                    "\n\t 3- Sair"
                    "\n\t\t Digite a opção: ")
                )
                if op == 1 or op == 2:
                    dados = op
                    break
                elif op == 3:
                    sair()
                else:
                    print("Opção inválida! Tente novamente...")
            # -
            print(separador())
            # -
            if dados == 2:
                executa(mapa_pronto, qual_dijkstra)

        else:
            mapa_novo = GrafoComPesos()
            print("|Dados do novo Mapa|\n---")
            # -
            print("|Insira o nome dos vértices do mapa.|")
            print("> Lembrando que o nome não pode exceder o limite de 6 caracteres!")
            cont = 1
            while True:
                print("-")
                v = input("> Digite o nome do vértice nº {} (ou \"sair\" para terminar): ".format(cont))
                if v == "sair":
                    break
                try:
                    mapa_novo.adicionaVertice(v)
                    cont += 1
                except VerticeInvalidoException:
                    print("> Ops! O vértice \'{}\' é inválido! "
                          "Lembre-se da regra da quantidade de caracteres... :)".format(v))
            # -
            print(separador())
            # -
            print("|Insira as arestas e seus pesos.|")
            print("> Lembrando que as arestas devem interligar dois vértices EXISTENTES no mapa "
                  "e deve ter o formato: \"X-Y\"!")
            cont = 1
            while True:
                print("-")
                aresta = input('> Digite a aresta nº {} (ou \'sair\' para terminar): '.format(cont))
                if aresta == "sair":
                    print("---")
                    print("Mapa criado!")
                    print(separador())
                    break
                peso = int(input('> Digite o peso da aresta nº {}: '.format(cont)))
                try:
                    mapa_novo.adicionaAresta(aresta, peso)
                    cont += 1
                except ArestaInvalidaException:
                    print("> Ops! A aresta \'{}\' é inválida! Lembre-se das regras... :)".format(aresta))

            executa(mapa_novo, qual_dijkstra)

    # ---

    if testando or dados == 1:
        # ------------- DADOS PRONTOS ------------- #
        print("|Matriz de Adjacência do Mapa|")
        print(mapa_pronto.matriz_sem_pesos())
        print("---")

        # --- .:: DADOS PRONTOS Dijkstra ::. --- #
        u_ = '1'
        v_ = '32'
        if testando or qual_dijkstra <= 1:
            caminho_mapa_pronto = mapa_pronto.dijkstra(u_, v_)
            if caminho_mapa_pronto:
                print('> Menor caminho entre {} e {} no Mapa usando Dijkstra: '.format(u_, v_), caminho_mapa_pronto)
            else:
                print("> Não foi possível encontrar um caminho de {} a {} para este Mapa usando Dijkstra! :(".format(u_,
                                                                                                                     v_)
                      )

        print("---")

        if testando or qual_dijkstra == 0 or qual_dijkstra == 2:
            # --- .:: DADOS PRONTOS Dijkstra Modificado ::. --- #
            carga_inicial_ = 3
            carga_maxima_ = 5
            ponto_inicial_ = '1'
            ponto_final_ = '32'
            pontos_de_recarga_ = ['12', '19', '21', '30']
            # -
            dados_iniciais(carga_maxima_, carga_inicial_, ponto_inicial_, ponto_final_, pontos_de_recarga_)
            # -
            melhor_caminho(carga_inicial_, carga_maxima_)
            print('>', mapa_pronto.dijkstra_mod(u_, v_, carga_inicial_, carga_maxima_, pontos_de_recarga_))
            # -

        print("---")
        # -

        if testando:
            break
