from Roteiro7.Roteiro7__funcoes import GrafoComPesos


# --------------------------------------------------------------------------- #
def atributos_finais(c_m, c_i, p_i, p_f, p_de_r):
    print("|Atributos Finais|\n---"
          "\n• Carga Máxima:", c_m,
          "\n• Carga Inicial:", c_i,
          "\n• Ponto Inicial:", p_i,
          "\n• Ponto Final:", p_f,
          "\n• Pontos de Recarga:", p_de_r)
    print("---")


def melhor_caminho(c_i, c_m):
    print('> Melhor caminho neste Mapa para o Drone com Carga Inicial {}: '.format('de {}'.format(c_i))
          if c_i < c_m else '{} ({})'.format('Máxima', c_m))


# --------------------------------------------------------------------------- #
mapa = GrafoComPesos()
# -
mapa_pronto = GrafoComPesos(
    ['1',  '2',   '3', '4',  '5',  '6',  '7',  '8',  '9', '10',
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


opt = int(input("> Digite \'1\' para usar o Mapa Pronto (ou qualquer outro número para criar um novo Mapa): "))
# ---
if opt != 1:
    print("|Dados do novo Mapa|\n---")
    # -
    vertices = [str(x) for x in input("> Insira o nome dos vértices (separados por espaço): ")]
    for v in vertices:
        mapa.adicionaVertice(v)
    # -
    print("Insira as arestas e seus pesos:")
    arestas = {}
    cont = 1
    while True:
        aresta = input('> Digite a aresta nº {} (ou 0 para terminar): '.format(cont))
        if aresta == 0:
            for a, p in arestas.items():
                mapa.adicionaAresta(a, p)
            break
        peso = int(input('> Digite o peso da aresta nº {}: '.format(cont)))
        arestas[aresta] = peso
        cont += 1

# ----
teste = int(input("> Digite \'1\' para usar os Dados Prontos (ou qualquer outro número para inserir novos dados): "))
print("---")

# ----
print("Matriz de Adjacência do Mapa:")
# -
if teste:
    print(mapa_pronto.matriz_sem_pesos())
    print("---")
    # -
    print('> Menor caminho do Mapa usando Dijkstra: ', mapa_pronto.dijkstra('1', '32'))
    print("---")

    # --- .:: DADOS PRONTOS ::. --- #
    carga_inicial = 3
    carga_maxima = 5
    ponto_inicial = '1'
    ponto_final = '32'
    pontos_de_recarga = ['12', '19', '21', '30']
    # -
    print(atributos_finais(carga_maxima, carga_inicial, ponto_inicial, ponto_final, pontos_de_recarga))
    # -
    print(melhor_caminho(carga_inicial, carga_maxima))
    print('>', mapa_pronto.dijkstra_mod(ponto_inicial, ponto_final, carga_inicial, carga_maxima, pontos_de_recarga))
    # -
    exit(0)


# ----
print(mapa.matriz_sem_pesos())
print("---")
# -
print('> Menor caminho do Mapa usando Dijkstra: ', mapa.dijkstra('1', '32'))
print("---")


# ----
print("|Atributos Iniciais do Drone|\n---")
# -
carga_maxima = int(input("> Digite a Capacidade Máxima de Carga do Drone: "))
# -
carga_inicial = int(input("> Digite Carga Inicial: "))
print("---")


# ----
print("|Atributos iniciais do Mapa|\n---")
# -
while True:
    ponto_inicial = input("> Digite o Ponto de Partida: ")
    if not mapa.existeVertice(ponto_inicial):
        print("O vértice \"{}\" não existe no mapa! Tente novamente...".format(ponto_inicial))
    else:
        break
# -
while True:
    ponto_final = input("> Digite o Ponto de Destino: ")
    if not mapa.existeVertice(ponto_final):
        print("O vértice \"{}\" não existe no mapa! Tente novamente...".format(ponto_final))
    else:
        break
# -
quantidade = int(input("> Digite a quantidade de Pontos de Recarga: "))
# -
pontos_de_recarga = []
for x in range(quantidade):
    while True:
        vertice = input("> Digite o Ponto de Recarga nº {} (ou \"sair\" quando terminar): ".format(x))
        if vertice != "sair":
            if not mapa.existeVertice(vertice):
                print("O vértice \"{}\" não existe no mapa! Tente novamente...".format(vertice))
            else:
                pontos_de_recarga[x] = vertice
                break
        else:
            break
    if vertice == "sair":
        break
print("---")


# ----
print(atributos_finais(carga_maxima, carga_inicial, ponto_inicial, ponto_final, pontos_de_recarga))

# ----
print(melhor_caminho(carga_inicial, carga_maxima))
print('>', mapa.dijkstra_mod(ponto_inicial, ponto_final, carga_inicial, carga_maxima, pontos_de_recarga))
