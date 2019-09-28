from Roteiro5.Roteiro5__funcoes import Grafo


class Grafos:

    # --- | Pontes de Königsberg | --- #
    konigsberg = Grafo()
    for v in ['M', 'T', 'B', 'R']:
        konigsberg.adicionaVertice(v)
    for a in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
        konigsberg.adicionaAresta(a)

    konigsberg_mod = Grafo()
    for v in ['M', 'T', 'B', 'R']:
        konigsberg_mod.adicionaVertice(v)
    for a in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
        konigsberg_mod.adicionaAresta(a)

    # --- | Grafos da Paraíba | --- #
    paraiba = Grafo()
    for v in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        paraiba.adicionaVertice(v)
    for a in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        paraiba.adicionaAresta(a)

    paraiba_sem_paralelas = Grafo()
    for v in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        paraiba_sem_paralelas.adicionaVertice(v)
    for a in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        paraiba_sem_paralelas.adicionaAresta(a)

    paraiba_euler = Grafo()
    for v in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        paraiba_euler.adicionaVertice(v)
    for a in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'M-T', 'T-Z']:
        paraiba_euler.adicionaAresta(a)

    # --- | Grafos Eulerianos | --- #
    euleriano = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        euleriano.adicionaVertice(v)
    for a in ['A-B', 'A-F', 'B-C', 'B-G', 'B-F', 'F-E', 'F-G', 'G-C', 'G-E', 'E-C', 'E-D', 'D-C']:
        euleriano.adicionaAresta(a)

    euleriano_2 = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        euleriano_2.adicionaVertice(v)
    for a in ['A-B', 'A-F', 'B-F', 'B-G', 'B-C', 'F-G', 'F-E', 'G-C', 'G-E', 'C-E', 'C-D', 'E-D']:
        euleriano_2.adicionaAresta(a)

    hexagono = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        hexagono.adicionaVertice(v)
    for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-F', 'F-A']:
        hexagono.adicionaAresta(a)

    # --- | Grafos Semi-Eulerianos | --- #
    semi_euler = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
        semi_euler.adicionaVertice(v)
    for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-B', 'B-D', 'B-F', 'F-H', 'H-G', 'G-I', 'I-J', 'J-K', 'J-A', 'J-G', 'K-G',
              'A-G', 'B-G']:
        semi_euler.adicionaAresta(a)

    semi_euler_com_lacos = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
        semi_euler_com_lacos.adicionaVertice(v)
    for a in ['A-A', 'A-B', 'B-C', 'C-D', 'D-E', 'D-D', 'E-B', 'B-D', 'B-F', 'F-H', 'H-G', 'G-I', 'I-J', 'J-K', 'J-A',
              'J-G', 'K-G', 'A-G', 'B-G']:
        semi_euler_com_lacos.adicionaAresta(a)

    semi_euler_2 = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E']:
        semi_euler_2.adicionaVertice(v)
    for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-C']:
        semi_euler_2.adicionaAresta(a)

    semi_euler_3 = Grafo()
    for v in ['1', '2', '3', '4', '5', '6', '7']:
        semi_euler_3.adicionaVertice(v)
    for a in ['1-2', '2-3', '3-4', '4-5', '5-3', '3-6', '6-7', '7-3']:
        semi_euler_3.adicionaAresta(a)

    # --- | Grafos Hamiltonianos | --- #

    # --- | Outros | --- #
    ex_graph = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
        ex_graph.adicionaVertice(v)
    for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-B', 'B-D', 'B-F', 'F-H', 'H-G', 'G-I', 'I-J', 'J-K', 'J-A', 'J-G', 'K-G',
              'A-G', 'B-G']:
        ex_graph.adicionaAresta(a)
