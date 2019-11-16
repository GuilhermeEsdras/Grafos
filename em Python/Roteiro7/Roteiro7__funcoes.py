from Roteiro7.Roteiro7__exceptions import *


# .:: Arquivo principal onde se encontram as funções referentes ao Roteiro 7 ::. #
# --------------------------------------------------------------------------- #
class GrafoComPesos:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, A=None):
        """
        Constrói um objeto do tipo Grafo Direcionado com Pesos.
        :param V: Uma Lista com os Vértices (ou nodos) do Grafo.
        :param A: Um Dicionário, onde cada chave (key) é uma String representando a aresta, e cada valor (value) desta
                  chave, é um inteiro representando o peso desta aresta.
        """

        # Cria a lista de vértices vazia caso não seja passada uma como argumento:
        if not V:
            V = list()

        # Para cada vértice passado como argumento, verifica se são válidos:
        for v in V:
            if not (GrafoComPesos.verticeValido(v)):
                # Levanta exceção caso não seja válido:
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                # Atualiza tamanho do nome do maior vértice para ajustar a matriz:
                self.__maior_vertice = len(v)

        # N (Lista de vértices do grafo) recebe os vértices passados como argumento (ou uma lista vazia):
        self.N = list(V)

        # Inicia a matriz de adjacência vazia:
        self.M = list()
        # Cria as listas das linhas de acordo com a quantidade vértices:
        for linha in range(len(V)):
            self.M.append(list())
            # Para cada célula da matriz cria uma lista que conterá a aresta e seu peso:
            for coluna in range(len(V)):
                self.M[linha].append([0, 0])

        # Caso tenha sido passado o dicionário com as arestas e pesos, cria a matriz com os dados:
        if A:
            for aresta in A.keys():
                if self.arestaValida(aresta):
                    peso = A[aresta]
                    if self.pesoValido(peso):
                        self.adicionaAresta(aresta, peso)
                    else:
                        raise PesoInvalidoException('O peso ' + peso + ' é inválido!')
                else:
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida!')

    def __primeiro_vertice_aresta(self, a: str):
        """
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        """
        return a[0:a.index(GrafoComPesos.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        """
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        """
        return a[a.index(GrafoComPesos.SEPARADOR_ARESTA) + 1:]

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

    @classmethod
    def verticeValido(self, vertice: str):
        """
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        Um vértice também não pode conter mais que 6 caracteres.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        """
        return vertice != '' and vertice.count(GrafoComPesos.SEPARADOR_ARESTA) == 0 and len(vertice) <= 6

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
        if aresta.count(GrafoComPesos.SEPARADOR_ARESTA) != GrafoComPesos.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(GrafoComPesos.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == GrafoComPesos.SEPARADOR_ARESTA:
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

    def existeVertice(self, vertice: str):
        """
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        """
        return GrafoComPesos.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, a: str):
        """
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param a: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        """
        return True \
            if self.arestaValida(a) and \
               self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)][0] \
            else False

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
                    self.M[k].append([0, 0])  # adiciona as listas de zeros (arestas e pesos) na coluna do vértice
                self.M[self.N.index(v)].append([0, 0])  # adiciona as listas de zeros na linha do vértice
        else:
            raise VerticeInvalidoException('O vértice {} é inválido'.format(v))

    def adicionaAresta(self, a, p):
        """
        Adiciona uma aresta e seu respectivo peso ao grafo, onde aresta deve estar no formato X-Y, onde X é o primeiro
        vértice e Y é o segundo vértice, e o peso sendo maior que zero.
        :param a: A aresta no formato correto
        :param p: O peso da aresta (inteiro maior que zero)
        :raises: Lança uma exceção caso a aresta não esteja em um formato válido ou o peso esteja abaixo do exigido
        """
        if self.existeAresta(a):
            raise ArestaExistenteException('A aresta {} já existe'.format(a))
        if self.arestaValida(a):
            if self.pesoValido(p):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                self.M[i_a1][i_a2][0], self.M[i_a1][i_a2][1] = 1, p
            else:
                raise PesoInvalidoException('O peso {} é inválido'.format(p))
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        """
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não esteja em um formato válido
        """
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                self.M[i_a1][i_a2][0], self.M[i_a1][i_a2][1] = 0, 0
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
        return self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)][1]

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
                    i_a1 = self.__indice_primeiro_vertice_aresta(a)
                    i_a2 = self.__indice_segundo_vertice_aresta(a)
                    self.M[i_a1][i_a2][1] = p
                else:
                    raise PesoInvalidoException('O peso {} é inválido'.format(p))
            else:
                raise ArestaNaoExistenteException('A aresta {} não existe'.format(a))
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    '''
    Funções auxiliares para um Grafo do tipo Matriz de Adjacência
    '''
    def pos(self, v):
        """
        :param v: Vértice.
        :return: Int. Posição/index do vértice v na lista de vértices (N) do GrafoComPesos.
        """
        return self.N.index(v)

    # ---

    '''
    - Roteiro 7 - Dijkstra, Inicio -
    '''

    def dijkstra(self, u, v):
        """
        Algoritmo de Dijkstra que encontra o caminho mais curto (considerando os pesos das arestas) entre u e v.
        :param u: Vértice de partida
        :param v: Vértice final
        :return: Uma Lista com o caminho
        """
        # Biblioteca(s) auxiliar(es)
        import math

        # Variável(is) auxiliar(es)
        vertices = self.N

        # Lista que armazenará as arestas indicando o menor caminho
        menor_caminho = []

        # Dicionários representando os rótulos do algoritmo para cada vértice
        Beta = {}  # Peso do menor caminho entre u e r
        Fi   = {}  # Marca cada vértice como permanente (1) ou temporário (0)
        Pi   = {}  # Predecessor de r no caminho u-r, se esse caminho existir, ou 0 se não existir

        # Inicializa os dicionários com os valores iniciais
        for r in vertices:
            if r != u:
                Beta[r] = math.inf  # 𝞫(r) ⇽ ∞
                Fi[r]  = 0          # 𝞿(r) ⇽ 0
            else:
                Beta[r] = 0  # 𝞫(u) ⇽ 0
                Fi[r]  = 1   # 𝞿(u) ⇽ 1

            Pi[r] = 0  # 𝞹(r) ⇽ 0

        w  = u
        r_ = 0  # r*
        while w != v:

            # Analisa os vértices de destino cuja aresta parte de w e atualiza seus beta's e pi's:
            for linha in range(len(vertices)):
                if linha == self.pos(w):
                    for coluna in range(len(vertices)):
                        # Para cada aresta partindo de w:
                        if self.M[linha][coluna][0] > 0:
                            r = vertices[coluna]        # Vértice vizinho de W a ser analisado / Vértice de destino
                            aresta = self.aresta(w, r)  # arco(w, r)
                            if Fi[r] == 0:
                                beta_do_antecessor_mais_arco = Beta[w] + self.alpha(aresta)  # alpha é o PesoDaAresta
                                # Se: Beta(r) for maior que Beta(w) + PesoDaAresta(w, r)  (𝞫(r) > 𝞫(w) + 𝞪(w,r))
                                if Beta[r] > beta_do_antecessor_mais_arco:
                                    # Então: 𝞫(r) ⇽ 𝞫(w) + 𝞪(w,r) e 𝞹(r) ⇽ w
                                    Beta[r] = beta_do_antecessor_mais_arco
                                    Pi[r] = w

            # Encontra o vértice r* tal que: 𝞿(r*) = 0, 𝞫(r*) < ∞ e 𝞫(r*) = menor beta dos betas:
            menor_beta = math.inf  # menor_beta inicia valendo infinito
            r_de_menor_beta = ''

            # Para cada r (vértice) e seu respectivo Beta no Dicionário de Beta's:
            for r, beta in Beta.items():
                # Se: 𝞿(r) = 0
                if Fi[r] == 0:
                    # Se 𝞫(r) < ∞ e 𝞫(r) = menor beta dos betas
                    if beta < menor_beta:
                        menor_beta = beta    # Passa a ser o menor beta
                        r_de_menor_beta = r  # Passa a ser o r com menor beta

            if menor_beta == math.inf:  # Se sair do loop e menor_beta ainda estiver valendo infinito...
                # r* não existe, então não há caminho u-v e o algoritmo deve parar
                return False

            # Caso contrário, r* se torna o r de menor beta com phi = 0:
            r_ = r_de_menor_beta

            # Atualiza as variáveis:
            Fi[r_] = 1  # 𝞿(r*) = 1 (torna o vértice permanente)
            w = r_       # w = r* (vértice a ser analisado no próximo loop)

        # Percorre o Dicionário de Pi's mostrando o menor caminho
        atual = v
        prox = Pi[atual]
        while True:
            menor_caminho.append(self.aresta(prox, atual))
            if prox == u:
                break
            else:
                atual = prox
                prox = Pi[atual]

        menor_caminho.reverse()
        return menor_caminho

    def dijkstra_mod(self, u, v, carga_inicial, carga_maxima, pontos_de_recarga=None):
        """
        Algoritmo de Dijkstra modificado para encontrar a melhor rota para um drone, baseando-se em pontos de recarga
        e seu nível de bateria.
        :param u: O vértice de onde o drone deve partir
        :param v: O vértice onde o drone deve chegar
        :param carga_inicial: A carga inicial da bateria
        :param carga_maxima: A carga máxima da bateria
        :param pontos_de_recarga: Uma lista de vértices que indicam os pontos de recarga
        :return: Uma Lista com as arestas indicando o melhor caminho
        """
        if pontos_de_recarga is None:
            pontos_de_recarga = []

        # Biblioteca(s) auxiliar(es)
        import math

        # Variável(is) auxiliar(es)
        vertices = self.N
        self.testando(False)  # TODO: FUNÇÃO INCOMPLETA/EM CONSTRUÇÃO/VAI DAR ERRO SE FOR TENTAR RODAR! :) #

        # Lista que armazenará as arestas indicando o melhor caminho
        melhor_caminho = []

        # Dicionários representando os rótulos do algoritmo para cada vértice
        Beta = {}  # Peso do menor caminho entre u e r
        Fi   = {}  # Marca cada vértice como permanente (1) ou temporário (0)
        Pi   = {}  # Predecessor de r no caminho u-r, se esse caminho existir, ou 0 se não existir
        Gama = {}  # Armazena a carga do drone em vértice

        # Inicializa os dicionários com os valores iniciais
        for r in vertices:
            if r != u:
                Beta[r] = math.inf  # 𝞫(r) ⇽ ∞
                Fi[r] = 0           # 𝞿(r) ⇽ 0
                Gama[r] = math.inf  # γ(r) ⇽ ∞
            else:
                Beta[r] = 0              # 𝞫(u) ⇽ 0
                Fi[r]   = 1              # 𝞿(u) ⇽ 1
                Gama[r] = carga_inicial  # γ(r) ⇽ Carga Inicial

            Pi[r]   = 0         # 𝞹(r) ⇽ 0

        w = u
        r_ = 0  # r*
        while w != v:

            # Analisa os vértices de destino cuja aresta parte de w e atualiza seus beta's e pi's:
            for linha in range(len(vertices)):
                if linha == self.pos(w):
                    for coluna in range(len(vertices)):
                        # Para cada aresta partindo de w:
                        if self.M[linha][coluna][0] > 0:
                            r = vertices[coluna]  # Vértice vizinho de W a ser analisado / Vértice de destino
                            aresta = self.aresta(w, r)  # arco(w, r)
                            if Fi[r] == 0:
                                PesoDaAresta = self.alpha(aresta)
                                beta_do_antecessor_mais_arco = Beta[w] + PesoDaAresta
                                # Se: Beta(r) for maior que Beta(w) + PesoDaAresta(w, r)  (𝞫(r) > 𝞫(w) + 𝞪(w,r))
                                if Beta[r] > beta_do_antecessor_mais_arco and Gama[w] >= PesoDaAresta:
                                    # Então: 𝞫(r) ⇽ 𝞫(w) + 𝞪(w,r) e 𝞹(r) ⇽ w
                                    Beta[r] = beta_do_antecessor_mais_arco
                                    Pi[r] = w
                                    # E se r for um ponto de recarga: γ(r) ⇽ Carga Máxima
                                    if r in pontos_de_recarga:
                                        Gama[r] = carga_maxima
                                    # senão: γ(r) ⇽ Carga no ponto anterior - 1 (perde 1 ponto de carga)
                                    else:
                                        Gama[r] = Gama[w] - 1

            # Encontra o vértice r* tal que: 𝞿(r*) = 0, 𝞫(r*) < ∞ e 𝞫(r*) = menor beta dos betas:
            menor_beta = math.inf  # menor_beta inicia valendo infinito
            r_de_menor_beta = ''

            # Para cada r (vértice) e seu respectivo Beta no Dicionário de Beta's:
            for r, beta in Beta.items():
                # Se: 𝞿(r) = 0
                if Fi[r] == 0:
                    # Se 𝞫(r) < ∞ e 𝞫(r) = menor beta dos betas
                    if beta < menor_beta:
                        menor_beta = beta  # Passa a ser o menor beta
                        r_de_menor_beta = r  # Passa a ser o r com menor beta

            if menor_beta == math.inf:  # Se sair do loop e menor_beta ainda estiver valendo infinito...
                # r* não existe, então não há caminho u-v e o algoritmo deve parar
                return False

            # Caso contrário, r* se torna o r de menor beta com phi = 0:
            r_ = r_de_menor_beta

            # Atualiza as variáveis:
            Fi[r_] = 1  # 𝞿(r*) = 1 (torna o vértice permanente)
            w = r_      # w = r* (vértice a ser analisado no próximo loop)

        # Percorre o Dicionário de Pi's mostrando o menor caminho
        atual = v
        prox = Pi[atual]
        while True:
            melhor_caminho.append(self.aresta(prox, atual))
            if prox == u:
                break
            else:
                atual = prox
                prox = Pi[atual]

        melhor_caminho.reverse()
        return melhor_caminho

    '''
    - Roteiro 7 - Dijkstra, Fim -
    '''

    def matriz_sem_pesos(self):
        """
        Fornece uma representação do tipo String (como Matriz de Adjacência sem Pesos) do grafo.
        :return: Uma string que representa o grafo
        """
        # Dá o espaçamento inicial do canto da borda superior esquerda
        espaco = ' ' * self.__maior_vertice

        grafo_str = espaco

        # Printa e ajusta o cabeçalho:
        for v in range(len(self.N)):
            grafo_str += ' '
            grafo_str += '{}'.format(self.N[v]).center(len(self.N[v]))

        grafo_str += '\n'

        # Printa e ajusta as linhas:
        for l in range(len(self.M)):
            # Printa e ajusta o espaçamento do nome do vértice de cada linha
            grafo_str += '{}'.format(self.N[l]).rjust(self.__maior_vertice) + ' '

            # Printa cada número de aresta
            for c in range(len(self.M)):
                grafo_str += '{}'.format(str(self.M[l][c][0])).center(len(self.N[c]))

                # Dá o espaçamento entre cada número, apenas se não for o último da linha
                if c != len(self.M) - 1:
                    grafo_str += ' '

            grafo_str += '\n'

        return grafo_str

    def testando(self, err):
        err = True
        if err:
            raise IncompletoException("A FUNÇÃO ESTÁ INCOMPLETA '-' -> EU AVISEI NA LINHA 391 QUE IA DAR ERRO!!!! :)")

    def __str__(self):
        """
        Fornece uma representação do tipo String (como Matriz de Adjacência contendo Pesos) do grafo.
        :return: Uma string que representa o grafo
        """
        # Dá o espaçamento inicial do canto da borda superior esquerda
        grafo_str = ' ' * self.__maior_vertice

        # Printa e ajusta o cabeçalho:
        for i, v in enumerate(self.N):
            grafo_str += ' '
            grafo_str += '{}'.format(v).center(6)

        grafo_str += '\n'

        # Ajusta o espaçamento de cada linha
        for l in range(len(self.M)):
            # Printa e ajusta o espaçamento do nome do vértice de cada linha
            grafo_str += '{}'.format(self.N[l]).rjust(self.__maior_vertice) + ' '

            # Printa cada lista contendo a aresta e seu peso
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c])

                # Dá o espaçamento entre cada lista, apenas se não for o último da linha
                if c != len(self.M) - 1:
                    grafo_str += ' '

            grafo_str += '\n'

        return grafo_str


class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        """
        Constrói um objeto do tipo Grafo Direcionado. Se nenhum parâmetro for passado, cria um Grafo vazio.
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
                    M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se a matriz é do tipo Direcionada
                '''
                if i > j and (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz representa uma matriz não direcionada')

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
                    self.M[k].append(0)  # adiciona os zeros na coluna do vértice
                self.M[self.N.index(v)].append(0)  # adiciona os zeros na linha do vértice
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
            self.M[i_a1][i_a2] += 1
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
                self.M[i_a1][i_a2] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

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


class IncompletoException(Exception):
    pass
