from Roteiro8.Roteiro8__exceptions import *


# .:: Arquivo principal onde se encontram as funções referentes ao Roteiro 7 ::. #
# --------------------------------------------------------------------------- #
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

        self.N   = list(V)
        self.__P = {}  # Dicionário que armazena os Pesos de cada aresta

        if not M:
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

    def pesoValido(self, peso):
        """
        Verifica se o peso passado como parâmetro é válido (verifica se o peso é maior que zero).
        :param peso: Valor inteiro.
        :return: Valo booleano.
        """
        return peso > 0

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
            self.__P[a] = 1
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def adicionaArestaComPeso(self, a, p):
        """
        Adiciona uma aresta (no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice) com peso ao grafo.
        :param a: a aresta no formato correto
        :param p: o peso da aresta
        :raise: lança uma exceção caso a aresta não estiver em um formato válido ou o peso seja igual a zero
        """
        if self.arestaValida(a):
            if self.pesoValido(p):
                self.__P[a] = p
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] += 1
                else:
                    self.M[i_a2][i_a1] += 1
            else:
                raise PesoInvalidoException('O peso {} é inválido'.format(p))
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
                self.__P.pop(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def aresta(self, v1, v2):
        """
        :param v1: Vértice 1.
        :param v2: Vértice 2.
        :return: Aresta devidamente formatada.
        """
        return '{}{}{}'.format(v1, self.SEPARADOR_ARESTA, v2)

    def alpha(self, a):
        """
        Retorna o Peso da aresta passada como parâmetro.
        :param a: Aresta
        :return: Inteiro
        """
        if self.arestaValida(a):
            if self.existeAresta(a):
                try:
                    return self.__P[a]
                except KeyError:
                    a_inv = self.aresta(self.N[self.__indice_segundo_vertice_aresta(a)],
                                        self.N[self.__indice_primeiro_vertice_aresta(a)])
                    return self.__P[a_inv]
            else:
                raise ArestaNaoExistenteException('A aresta {} não existe'.format(a))
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def modifica_peso(self, a, p):
        """
        Modifica o Peso de uma determinada Aresta.
        :param a: a aresta no formato correto
        :param p: o novo peso maior que zero
        :raises: lança uma exceção caso a aresta seja inválida ou o peso esteja abaixo do exigido
        """
        if self.arestaValida(a):
            if self.existeAresta(a):
                if self.pesoValido(p):
                    self.__P[a] = p
                else:
                    raise PesoInvalidoException('O peso {} é inválido'.format(p))
            else:
                raise ArestaNaoExistenteException('A aresta {} não existe'.format(a))
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def peso(self, v1, v2):
        """
        Retorna o peso da aresta formada pelos vértices v1 e v2
        :param v1: Vértice de partida
        :param v2: Vértice de destino
        :return: Inteiro como peso da aresta ou False caso a aresta não exista
        """
        if self.existeAresta(self.aresta(v1, v2)):
            try:
                return self.__P[self.aresta(v1, v2)]
            except KeyError:
                return self.__P[self.aresta(v2, v1)]
        else:
            return False

    def pesos(self):
        """
        :return: Retorna o dicionário de pesos das arestas do Grafo.
        """
        return self.__P

    def pos(self, v):
        """
        :param v: Vértice.
        :return: Int. Posição/index do vértice v na lista de vértices (N) do GrafoComPesos.
        """
        return self.N.index(v)

    def menor_aresta(self):
        """
        Retorna a aresta detentora do menor Peso no Grafo.
        :return: String que representa a aresta no formato "x-y"
        """
        menor_aresta = ''
        menor_peso   = 0
        for aresta, peso in self.__P.items():
            if peso > menor_peso:
                menor_peso   = peso
                menor_aresta = aresta
        return menor_aresta

    def maior_aresta(self):
        """
        Retorna a aresta detentora do maior Peso no Grafo.
        :return: String que representa a aresta no formato "x-y"
        """
        maior_aresta = ''
        maior_peso   = 0
        for aresta, peso in self.__P.items():
            if peso > maior_peso:
                maior_peso   = peso
                maior_aresta = aresta
        return maior_aresta

    def vertices_adjacentes(self, v):
        """
        Retorna uma lista com todos os vértices adjacentes (vizinhos) ao vértice v no Grafo.
        :param v: Vértice de origem
        :return: Lista contendo todos os vértices de destino em relação a v
        """
        adjacentes = []
        for v1 in range(len(self.N)):
            for v2 in range(len(self.N)):
                if v1 == self.pos(v) and v2 >= self.pos(v):
                    if self.M[v1][v2] > 0:
                        adjacentes.append(self.N[v2])
        return adjacentes

    # ---

    def ha_ciclo_aux(self, v):
        visitado = {v: False for v in self.N}
        pilha = [v]
        while pilha:
            vertice = pilha.pop()
            if visitado[vertice]:
                return True
            visitado[vertice] = True
            pilha.extend(self.vertices_adjacentes(vertice))
        return False

    def ha_ciclo(self):
        for v in self.N:
            if self.ha_ciclo_aux(v):
                return True
        return False

    # ---

    def eh_aresta_segura(self, a):
        """
        Uma Aresta Segura, ou Safe Edge, é uma aresta na qual não cria um loop/ciclo no grafo.
        :param a: Aresta
        :return: Valor booleano. True se não criar um ciclo, ou False caso contrário.
        """
        return

    '''
    - Roteiro 8 - Minimum Spanning Tree, Inicio -
    '''

    def kruskal(self):
        from copy import deepcopy
        from math import inf

        T = Grafo()
        for v in self.N:
            T.adicionaVertice(v)

        E = deepcopy(self.__P)

        while E:
            menor_aresta = ''
            menor_peso   = inf
            for aresta, peso in E.items():
                if peso < menor_peso:
                    menor_peso   = peso
                    menor_aresta = aresta
            E.pop(menor_aresta)
            T.adicionaArestaComPeso(menor_aresta, menor_peso)
            if T.ha_ciclo():
                T.remove_aresta(menor_aresta)

        return T

    def kruskal_mod(self):
        return

    # ---

    def prim(self):

        return

    def prim_mod(self):
        from copy import deepcopy
        from math import inf

        V = deepcopy(self.N)
        E = deepcopy(self.__P)
        Jet = {}
        P   = {}

        for x in V:
            Jet[x] = inf
            P[x]   = None

        menor_aresta = ''
        menor_peso   = inf
        for aresta, peso in E:
            if peso < menor_peso:
                menor_peso   = peso
                menor_aresta = aresta

        Jet[menor_aresta] = 0

        Q = deepcopy(V)
        while Q:
            menor_vertice = ''
            menor_valor   = inf
            for vertice, value in Jet.items():
                if value < menor_valor:
                    menor_valor   = value
                    menor_vertice = vertice
            x = Q.pop(menor_vertice)

            for vizinho in self.vertices_adjacentes(x):
                Jet[vizinho] = self.peso(x, vizinho)
        return

    '''
    - Roteiro 8 - Minimum Spanning Tree,, Fim -
    '''

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
