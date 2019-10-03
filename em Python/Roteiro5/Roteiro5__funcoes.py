# -*- coding: utf-8 -*-


class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        """
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param M: Uma matriz de adjacência que guarda as arestas do grafo.
                  Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        """

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k > l:
                        M[k].append('-')
                    else:
                        M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not (self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        """
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        """

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        """
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        """
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        """
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        """
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        """
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        """
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        """
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        """
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        """
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        """
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        """
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        """
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        """
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param a: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        """
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        """
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        """
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-')  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        """
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        """
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        """
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        """
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    # ---

    '''
    - Funções Auxiliares, Inicio -
    '''

    def pos(self, v):
        """
        :param v: Vértice.
        :return: Int. Posição/index do vértice v na lista de vértices (N) do Grafo.
        """
        return self.N.index(v)

    def vizinhos_do_vertice(self, v):
        """
        :param v: Vértice.
        :return: Uma lista contendo os vértices vizinhos de v.
        """
        vertices = []
        for linha, arestas in enumerate(self.M):
            for coluna, qtd in enumerate(arestas):
                if qtd != '-' and qtd > 0:
                    if linha < self.pos(v):
                        if coluna == self.pos(v):
                            vertices.append(self.N[linha])
                    elif linha == self.pos(v):
                        vertices.append(self.N[coluna])
                    else:
                        break
        return vertices

    def remove_vertice(self, v):
        """
        Remove um determinado vértice do grafo.
        :param v: Vértice a ser excluído
        """
        if self.verticeValido(v):
            for i, x in enumerate(self.M):
                if i == self.pos(v):
                    x.clear()
                else:
                    x.pop(self.pos(v))
            self.M = [x for x in self.M if x != []]
            self.N.remove(v)
        else:
            raise VerticeInvalidoException('O vértice {} é inválido'.format(v))

    def aresta(self, v1, v2):
        """
        :param v1: Vértice 1.
        :param v2: Vértice 2.
        :return: Aresta devidamente formatada.
        """
        return '{}{}{}'.format(v1, self.SEPARADOR_ARESTA, v2)

    def existe_caminho(self, v1, v2):
        """
        Verifica se existe um caminho entre os dois vértices (v1 e v2).
        :param v1: Vértice 1.
        :param v2: Vértice 2.
        :return: Valor Booleano. True se existir, False caso contrário.
        """
        if not self.existeVertice(v1) or not self.existeVertice(v2) or \
                not self.vizinhos_do_vertice(v1) or not self.vizinhos_do_vertice(v2):
            # Caso não exista um dos vértices no Grafo  OU  um dos vértices não possuir vizinhos:
            return False

        visitado = [False] * (len(self.N))  # Marca todos os vértices como não visitados.
        aux = []  # Lista auxiliar.
        aux.append(v1)  # Adiciona o vértice 1 a lista auxiliar para começar procurando a partir dos vizinhos dele.

        while aux:  # Enquanto houverem vértices alcançáveis a partir de v1 [vértice 1] a serem verificados:
            # Retira o elemento adicionado da lista aux e o verifica:
            vsv = aux.pop(0)  # vértice a ser verificado ( v.s.v )
            if vsv == v2:  # Se o v.s.v for o vértice 2, existe um caminho entre v1 e v2.
                return True
            # Caso contrário, continua verificando os vizinhos e os vizinhos dos vizinhos do vértice 1:
            for v in self.vizinhos_do_vertice(vsv):
                # Para cada vizinho do v.s.v.:
                if not visitado[self.pos(v)]:  # Se ainda não foi visitado:
                    visitado[self.pos(v)] = True  # Marca-o como visitado
                    aux.append(v)  # Coloca na lista aux para ser verificado no próximo loop

        # Se todos os vértices alcançáveis a partir de v1 (vértice 1) foram visitados e não foi encontrado o vértice 2:
        return False  # Não existe um caminho entre v1 e v2.

    def eh_conexo(self):
        """
        Verifica se o grafo é conexo.
        Um Grafo é dito conexo caso exista um caminho possível entre quaisquer par de vértices dele.
        :return: Valor Booleano. True se for, False se não for.
        """
        for v1 in self.N:
            for v2 in self.N:
                if not self.existe_caminho(v1, v2):
                    return False
        return True

    def eh_uma_ponte(self, v1, v2):
        """
        Verifica se uma aresta é uma ponte.
        Uma aresta é chamada de ponte caso a sua remoção torne o grafo desconexo.
        :param v1: Vértice 1.
        :param v2: Vértice 2.
        :return: Valor Booleano.
        """
        aresta = self.aresta(v1, v2)
        self.remove_aresta(aresta)
        eh_uma_ponte = (not self.eh_conexo())
        self.adicionaAresta(aresta)
        return eh_uma_ponte

    def __caminhos_aux(self, v1, v2, visitado, caminho, caminhos):
        """
        Função auxiliar de "caminhos_entre_dois_vertices" que percorre o grafo recursivamente em busca de vários
        caminhos entre os vértices v1 e v2.
        :param v1: Vértice 1.
        :param v2: Vértice 2
        :param visitado: Lista com vértices visitados
        :param caminho: Lista com um caminho
        :param caminhos: Lista com todos os caminhos
        :return: None
        """
        visitado[self.pos(v1)] = True
        caminho.append(v1)

        if v1 == v2:
            caminho_aux = [x for x in caminho]
            caminho_com_aresta = []
            for i, v in enumerate(caminho_aux):
                caminho_com_aresta.append(v)
                if i != len(caminho_aux) - 1:
                    caminho_com_aresta.append(self.aresta(v, caminho_aux[i + 1]))
            caminhos.append(caminho_com_aresta)

        else:
            for i in self.vizinhos_do_vertice(v1):
                if not visitado[self.pos(i)]:
                    self.__caminhos_aux(i, v2, visitado, caminho, caminhos)

        caminho.pop()
        visitado[self.pos(v1)] = False

    def caminhos_entre_dois_vertices(self, v1, v2):
        """
        Percorre o grafo recursivamente em busca de vários caminhos entre v1 e v2.
        :param v1: Vértice 1.
        :param v2: Vértice 2.
        :return: Uma lista de listas com caminhos entre v1 e v2.
        """
        if not self.existe_caminho(v1, v2):
            return False
        if self.ha_laco():
            if v1 == v2:
                return [v1, self.aresta(v1, v2), v2]

        visitado = [False] * (len(self.N))
        caminhos = []
        self.__caminhos_aux(v1, v2, visitado, [], caminhos)
        return caminhos

    def menor_caminho(self, v1, v2):
        """
        Retorna o caminho mais curto encontrado entre v1 e v2.
        :param v1: Vértice 1
        :param v2: Vértice 2
        :return: Uma lista com o menor caminho
        """
        return self.caminhos_entre_dois_vertices(v1, v2)[-1]

    def __ha_ciclo_aux(self, v, visitado, pai):
        visitado[self.pos(v)] = True
        for vizinho in self.vizinhos_do_vertice(v):
            if not visitado[self.pos(vizinho)]:
                if self.__ha_ciclo_aux(vizinho, visitado, v):
                    return True
            elif pai != vizinho:
                return True
        return False

    def ha_ciclo(self):
        vertices = self.N
        visitado = [False] * (len(vertices))
        for vertice in vertices:
            if not visitado[self.pos(vertice)]:
                if self.__ha_ciclo_aux(vertice, visitado, ''):
                    return True
        return False

    def eh_laco(self, v):
        """
        Verifica se o vértice é/possui um laço.
        :param v: Vértice.
        :return: Valor Booleano. True se o vértice possuir ele mesmo como vizinho, ou False caso contrário.
        """
        return v in self.vizinhos_do_vertice(v)

    def vertices_grau_par(self):
        """
        :return: Lista com os vértices de grau par.
        """
        par = []
        for vertice in self.N:
            if self.grau(vertice) % 2 == 0:
                par.append(vertice)
        return par

    def vertices_grau_impar(self):
        """
        :return: Lista com os vértices de grau ímpar.
        """
        impar = []
        for vertice in self.N:
            if self.grau(vertice) % 2 != 0:
                impar.append(vertice)
        return impar

    def vertice_de_maior_grau(self):
        """
        Verifica qual(is) o(s) vértice(s) de maior grau.
        :return: Um vértice de maior grau. Caso haja mais de um, é retornado um aleatoriamente.
        """
        import random

        maior_grau = 0
        for vertice in self.N:
            grau = self.grau(vertice)
            if grau >= maior_grau:
                maior_grau = grau

        vertices_de_maior_grau = []
        for vertice in self.N:
            if self.grau(vertice) == maior_grau:
                vertices_de_maior_grau.append(vertice)

        return random.choice(vertices_de_maior_grau)

    def todas_as_arestas_do_grafo(self):
        """
        :return: Uma Lista contendo todas as arestas do Grafo.
        """
        arestas = []
        for linha, lista_de_arestas in enumerate(self.M):
            for coluna, qtd_de_arestas in enumerate(lista_de_arestas):
                if qtd_de_arestas != '-' and qtd_de_arestas > 0:
                    arestas.append(self.aresta(self.N[linha], self.N[coluna]))
        return arestas

    def remove_arestas_do_vertice(self, v):
        """
        Remove do grafo todas as arestas conectadas ao vértice v.
        :param v: Vértice.
        :return:
        """
        for vizinho in self.vizinhos_do_vertice(v):
            self.remove_aresta(self.aresta(v, vizinho))

    '''
    - Funções Auxiliares, Fim -
    '''

    # ---

    '''
    - Soluções do Roteiro 5, Inicio -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    def caminho_euleriano(self):
        """
        Verifica se o grafo possui um Caminho Euleriano e, em caso positivo, retorna uma lista contendo o caminho.
        Um Caminho Euleriano é um caminho que passa exatamente uma vez por cada aresta do grafo (pode passar mais de
        uma vez pelo mesmo vértice, mas não pela mesma aresta).
        :return: Uma lista representando o caminho.
        """
        if not self.eh_semi_euleriano():  # Verifica se o grafo tem os requisitos para possuir um caminho euleriano.
            return False
        import random

        grafo_aux = Grafo(self.N, self.M)
        caminho = []

        if grafo_aux.ha_laco():
            vertice_inicial = grafo_aux.vertice_de_maior_grau()
        elif len(grafo_aux.vertices_grau_impar()) > 0:
            while True:
                vertice_inicial = random.choice(grafo_aux.vertices_grau_impar())
                if not grafo_aux.eh_laco(vertice_inicial):
                    break
        else:
            vertice_inicial = grafo_aux.vertice_de_maior_grau()

        pvsv = grafo_aux.pos(vertice_inicial)  # Posição do Vértice a Ser Verificado ( p.v.s.v. )
        while True:
            vsv = grafo_aux.N[pvsv]  # Vértice a Ser Verificado ( v.s.v. )
            if len(caminho) > 0:
                if caminho[-1] != vsv:
                    caminho.append(vsv)
            else:
                caminho.append(vsv)

            if grafo_aux.grau(vsv) == 0:
                return caminho

            vizinhos = grafo_aux.vizinhos_do_vertice(vsv)
            for vizinho in vizinhos:
                if grafo_aux.eh_laco(vizinho) or len(vizinhos) == 1 or not grafo_aux.eh_uma_ponte(vsv, vizinho):
                    caminho.append(grafo_aux.aresta(vsv, vizinho))
                    grafo_aux.remove_aresta(grafo_aux.aresta(vsv, vizinho))
                    if grafo_aux.grau(vsv) == 0:
                        grafo_aux.remove_vertice(vsv)
                    pvsv = grafo_aux.pos(vizinho)
                    break

    def ciclo_hamiltoniano(self):
        """
        Retorna o caminho do ciclo de um Grafo com Ciclo Hamiltoniano.
        Um Ciclo Hamiltoniano é um Caminho Hamiltoniano fechado, ou seja, começa e termina no mesmo vértice.
        :return: Uma lista mostrando o ciclo, ou o valor Booleano False caso não exista.
        """
        import random

        grafo_aux = Grafo()
        grafo_aux.N = self.N.copy()
        grafo_aux.M = self.M.copy()

        vertices_iniciais_verificados = []
        ciclo = []
        visitado = [False] * len(self.N)

        vsv = random.choice(grafo_aux.N)  # Vértice a Ser Verificado ( v.s.v. )
        vertice_inicial = vsv
        vizinhos_do_inicial = grafo_aux.vizinhos_do_vertice(vsv)
        vertices_iniciais_verificados.append(vsv)
        tenta_outro_vertice = False
        while True:
            if not grafo_aux.eh_conexo():
                return False
            ciclo.append(vsv)
            visitado[self.pos(vsv)] = True
            vizinhos_de_vsv = grafo_aux.vizinhos_do_vertice(vsv)

            if visitado.count(True) == len(visitado) or tenta_outro_vertice:
                if not tenta_outro_vertice and vertice_inicial in vizinhos_de_vsv:
                    ciclo.append(grafo_aux.aresta(vsv, vertice_inicial))
                    ciclo.append(vertice_inicial)
                    return ciclo
                else:
                    visitado = [False] * len(self.N)
                    ciclo.clear()
                    # A partir daqui tá com erro, era pra "resetar" o grafo_aux e todas as outras variáveis, começando
                    # novamente com outro vértice inicial. Mas dá erro, não sei pq... ¯\_(ツ)_/¯
                    grafo_aux = Grafo()
                    grafo_aux.N = self.N.copy()
                    grafo_aux.M = self.M.copy()

                    while True:
                        vsv = random.choice(grafo_aux.N)
                        if vsv not in vertices_iniciais_verificados:
                            vertice_inicial = vsv
                            vizinhos_do_inicial = grafo_aux.vizinhos_do_vertice(vsv)
                            vertices_iniciais_verificados.append(vsv)
                            tenta_outro_vertice = False
                            break
                        elif len(vertices_iniciais_verificados) == len(grafo_aux.N):
                            return False

            else:
                encontrou = True
                ultima_chance = False
                menos_vizinhos = 0
                while True:
                    for i, vizinho in enumerate(vizinhos_de_vsv):
                        if vizinho not in ciclo:
                            grau_desse_vizinho = grafo_aux.grau(vizinho)
                            if grau_desse_vizinho < menos_vizinhos or menos_vizinhos == 0:
                                menos_vizinhos = grau_desse_vizinho
                            if ((vizinho not in vizinhos_do_inicial) or (not encontrou)) and \
                                    (grau_desse_vizinho <= menos_vizinhos):
                                ciclo.append(grafo_aux.aresta(vsv, vizinho))
                                if vsv != vertice_inicial:
                                    grafo_aux.remove_vertice(vsv)
                                vsv = vizinho
                                encontrou = True
                                break
                        if i == len(grafo_aux.vizinhos_do_vertice(vsv)) - 1:
                            encontrou = False
                    if encontrou:
                        break
                    else:
                        if not ultima_chance:
                            ultima_chance = True
                        else:
                            tenta_outro_vertice = True
                            return False
                            # break

    '''
    - Soluções do Roteiro 5, Fim -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    # --- | Outras Funções Referentes ao Roteiro 5 | --- #

    def eh_euleriano(self):
        """
        Verifica se o grafo é Euleriano, ou seja, se ele contém um Ciclo Euleriano.
        Um Grafo é considerado Euleriano se, e somente se, ele for conexo e todos os seus vértices possuirem grau par.
        :return: Valor Booleano. True se for, False em caso contrário.
        """
        if not self.eh_conexo():
            return False
        for vertice in self.N:
            if self.grau(vertice) % 2 != 0:
                return False
        return True

    def ciclo_euleriano(self):
        """
        Verifica se o grafo possui um Ciclo Euleriano.
        Um Ciclo Euleriano é um Caminho Euleriano fechado, ou seja, começa e termina no mesmo vértice.
        :return: Uma Lista contendo o Ciclo, ou o valor Booleano False caso não contenha.
        """
        if not self.eh_euleriano():
            return False
        while True:
            ciclo = self.caminho_euleriano()
            if ciclo[0] == ciclo[-1]:
                return ciclo

    def eh_semi_euleriano(self):
        """
        Verifica se o grafo é Semi-Euleriano.
        Um Grafo Semi-Euleriano é um grafo que não contém um ciclo euleriano, mas contém um caminho Euleriano.
        Um Grafo é considerado Semi-Euleriano se, e somente se, ele for conexo e possuir no máximo 2 vértices de
        grau ímpar.
        :return: Valor Booleano. True se for, False em caso contrário.
        """
        if not self.eh_conexo():
            return False
        vertices_grau_impar = 0
        for vertice in self.N:
            if self.grau(vertice) % 2 != 0 and not self.eh_laco(vertice):
                vertices_grau_impar += 1
            if vertices_grau_impar > 2:
                return False
        return True

    def caminho_hamiltoniano(self, v):
        """
        Verifica se o grafo possui um Caminho Hamiltoniano.
        Um Caminho Hamiltoniano é um caminho que passa exatamente uma vez por cada vértice (não importando se todas as
        arestas forem visitadas).
        :param: v: Vértice inicial.
        :return: Uma Lista contendo o caminho, ou o valor Booleano False caso não exista.
        """
        if not self.eh_conexo():
            return False

        caminho = []
        visitado = [False] * len(self.N)

        pvsv = self.pos(v)  # Posição do Vértice a Ser Verificado ( p.v.s.v. )
        while True:
            vsv = self.N[pvsv]  # Vértice a Ser Verificado ( v.s.v. )
            caminho.append(vsv)
            visitado[pvsv] = True

            if visitado.count(True) == len(visitado):
                return caminho

            encontrou = False
            for vizinho in self.vizinhos_do_vertice(vsv):
                if not visitado[self.pos(vizinho)]:
                    caminho.append(self.aresta(vsv, vizinho))
                    pvsv = self.pos(vizinho)
                    encontrou = True
                    break

            if not encontrou:
                return False

    def eh_hamiltoniano(self):
        """
        Verifica se o grafo é Hamiltoniano, ou seja, se existe um Ciclo Hamiltoniano.
        :return: Valor Booleano. True se for, False caso contrário.
        """
        return self.ciclo_hamiltoniano()

    # --- #

    '''
    - Soluções do Roteiro 4, Inicio -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    def vertices_nao_adjacentes(self):

        """
        Função que percorre a matriz do grafo em busca de pares de vértices não adjacentes.
        :return: Uma lista com todos os pares de vértices não adjacentes
        """
        # O loop percorre cada linha e verifica cada item desta linha.
        # Ao encontrar o valor 0, isso significa ausência de aresta entre os dois vértices, ou seja,
        # uma combinação de vértices não-adjacentes, então adiciona-os a lista de vertices_nao_adjacentes. E retorna-a.

        vertices_nao_adjacentes = []
        for x, lista_de_arestas in enumerate(self.M):
            for y, arestas in enumerate(lista_de_arestas):
                if arestas == 0:
                    vertices_nao_adjacentes.append(self.aresta(self.N[x], self.N[y]))
        return vertices_nao_adjacentes

    def ha_laco(self):

        """
        Função que verifica se o grafo possui um laço.
        :return: Valor booleano. True se sim, False caso contrário.
        """
        # O loop percorre a diagonal principal da matriz (ou seja, apenas o primeiro elemento após o traço '-' de cada
        # linha).
        # Se encontrar uma aresta (valor maior que 0) é porque possui laço, então retorna True.
        # Caso contrário, retorna False.

        for lista_de_arestas in self.M:
            for arestas in lista_de_arestas:
                if arestas != '-':
                    if arestas > 0:
                        return True
                    break
        return False

    def grau(self, v):

        """
        Função que retorna o grau de um vértice dado como parâmetro.
        :param v: Vértice.
        :return: Um inteiro que representa o grau do vértice.
        """
        # O loop percorre cada linha e cada coluna da matriz até a posição do vértice do parâmetro.
        # Então, soma o valor/quantidade das arestas conectadas aquele vértice, e adiciona-o a variável grau para depois
        # retorná-la.

        pos = self.pos(v)
        grau = 0
        for x, lista_de_arestas in enumerate(self.M):
            if x <= pos:
                for y, aresta in enumerate(lista_de_arestas):
                    if x != pos:
                        if y == pos:
                            grau += aresta
                    else:
                        if aresta != '-':
                            grau += aresta
        return grau

    def ha_paralelas(self):

        """
        Verifica se há arestas paralelas no grafo.
        :return: True se houver, ou False caso contrário.
        """
        # O loop verifica se há mais de uma aresta conectadas entre dois vértices, e em caso positivo retorna True.

        for lista_de_arestas in self.M:
            for arestas in lista_de_arestas:
                if arestas != '-' and arestas > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, v):

        """
        Função que verifica todos os vértices conectados ao vértice do parâmetro.
        :param v: Vértice.
        :return: Uma lista com todas as conexões do vértice do parâmetro
        """
        # O loop percorre a matriz do grafo em busca de conexões de outros vértices com o vértice do parâmetro.
        # Ou seja, ao encontrar um valor maior que 0 na posição em que se encontra o vértice do parâmetro, é adicionado
        # essa "conexão" a lista de vertices_incidentes

        pos = self.N.index(v)
        vertices_incidentes = []
        for x, lista_de_arestas in enumerate(self.M):
            if x <= pos:
                for y, arestas in enumerate(lista_de_arestas):
                    if x != pos:
                        if y == pos:
                            if arestas > 0:
                                for z in range(arestas):
                                    vertices_incidentes.append(self.aresta(self.N[x], self.N[y]))
                    else:
                        if arestas != '-':
                            if arestas > 0:
                                for z in range(arestas):
                                    vertices_incidentes.append(self.aresta(self.N[x], self.N[y]))
        return vertices_incidentes

    def eh_completo(self):

        """
        Função que verifica se o grafo é completo. Analisando se a quantidade de arestas está dentro do permitido.
        :return: Valor Booleano. True se for, False caso contrário
        """
        # Primeiro obtém-se a quantidade de vértices do grafo (n), para saber a quantidade máxima de arestas através do
        # Teorema que diz que o número de arestas em um grafo completo é n(n-1)/2.
        # Depois percorre a matriz verificando a quantidade de arestas do grafo.
        # Caso não encontre nenhuma aresta paralela e a quantidade de arestas esteja de acordo com o número máximo de
        # arestas permitidas para um grafo completo, retorna True. Caso contrário, retorna False

        n = len(self.N)
        if n == 1:
            return True

        max_de_arestas = (n * (n - 1)) // 2
        n_de_arestas = 0

        for lista_de_arestas in self.M:
            for arestas in lista_de_arestas:
                if arestas != '-':
                    if arestas > 1:
                        return False
                    else:
                        n_de_arestas += arestas

        if n_de_arestas == max_de_arestas or n_de_arestas == 2:
            return True

        return False

    '''
    - Soluções do Roteiro 4, Fim -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    def grafoParaPNG(self, nome):
        """
        Função que usa as bibliotecas NetworkX em conjunto com Matplotlib para gerar uma imagem do grafo.
        :param nome: Nome do arquivo de imagem do grafo que será salva.
        """
        try:
            import networkx as nx
            from matplotlib import pyplot as plt
        except Exception:
            raise

        grafo = nx.Graph()
        grafo.add_nodes_from(self.N)
        for aresta in self.todas_as_arestas_do_grafo():
            grafo.add_edge(aresta[0], aresta[2])
        nx.draw(grafo, with_labels=True)
        plt.savefig("{}.png".format(nome))

    def __str__(self):
        """
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        """

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * self.__maior_vertice

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str
