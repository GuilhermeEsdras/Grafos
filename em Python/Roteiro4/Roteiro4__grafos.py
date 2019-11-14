from Roteiro4.Roteiro4__funcoes import Grafo


class Grafos:
    
    # Grafo da Paraíba
    paraiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
    for aresta in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
        paraiba.adicionaAresta(aresta)
    
    # --- #
    
    # Grafo Completo
    grafo_completo = Grafo(['J', 'C', 'E', 'P'])
    for aresta in ['J-C', 'J-P', 'J-E', 'C-E', 'C-P', 'P-E']:
        grafo_completo.adicionaAresta(aresta)

    # --- #
    
    # K3
    k3 = Grafo(['A', 'B', 'C'])
    for aresta in ['A-B', 'B-C', 'C-A']:
        k3.adicionaAresta(aresta)

    # --- #
