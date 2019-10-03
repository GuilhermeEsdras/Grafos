from Roteiro5.Roteiro5__funcoes import Grafo


class Grafos:

    # --- | Bem Simples | --- #
    euleriano_bem_simples = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        euleriano_bem_simples.adicionaVertice(v)
    for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-F', 'F-G']:
        euleriano_bem_simples.adicionaAresta(a)

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

    # --- | Grafos Eulerianos / Hamiltonianos | --- #
    euleriano = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        euleriano.adicionaVertice(v)
    for a in ['A-B', 'A-F', 'B-C', 'B-G', 'B-F', 'F-E', 'F-G', 'G-C', 'G-E', 'E-C', 'E-D', 'D-C']:
        euleriano.adicionaAresta(a)

    euleriano_2 = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        euleriano_2.adicionaVertice(v)
    for a in ['A-D', 'A-E', 'D-E', 'E-B', 'E-F', 'B-F', 'F-C', 'F-G', 'C-G']:
        euleriano_2.adicionaAresta(a)

    hexagono = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        hexagono.adicionaVertice(v)
    for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-F', 'F-A']:
        hexagono.adicionaAresta(a)

    # --- | Com Ciclo Hamiltoniano | --- #
    com_ciclo_hamiltoniano = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        com_ciclo_hamiltoniano.adicionaVertice(v)
    for a in ['A-B', 'A-F', 'A-D', 'B-C', 'B-G', 'C-D', 'C-H', 'D-E', 'E-F', 'E-H', 'F-G', 'G-H']:
        com_ciclo_hamiltoniano.adicionaAresta(a)

    # --- | Grafos Semi-Eulerianos | --- #
    semi_euler = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        semi_euler.adicionaVertice(v)
    for a in ['A-B', 'A-C', 'B-C', 'C-D', 'D-E', 'E-F', 'E-G', 'F-G']:
        semi_euler.adicionaAresta(a)

    semi_euler_com_laco = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        semi_euler_com_laco.adicionaVertice(v)
    for a in ['A-A', 'A-B', 'A-C', 'B-C', 'C-C', 'C-D', 'D-D', 'D-E', 'E-F', 'E-G', 'F-G']:
        semi_euler_com_laco.adicionaAresta(a)

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

    # --- | Outros | --- #
    ex_graph = Grafo()
    for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
        ex_graph.adicionaVertice(v)
    for a in ['A-B', 'B-C', 'C-D', 'D-E', 'E-B', 'B-D', 'B-F', 'F-H', 'H-G', 'G-I', 'I-J', 'J-K', 'J-A', 'J-G', 'K-G',
              'A-G', 'B-G']:
        ex_graph.adicionaAresta(a)
