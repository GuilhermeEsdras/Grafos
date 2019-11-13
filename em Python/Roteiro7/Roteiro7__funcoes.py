class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class ArestaExistenteException(Exception):
    pass


class ArestaNaoExistenteException(Exception):
    pass


class PesoInvalidoException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


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

    # ---

    '''
    - Roteiro 7 - Dijkstra, Inicio -
    '''

    def Dijkstra(self, u, v):
        return True

    '''
    - Roteiro 7 - Dijkstra, Fim -
    '''

    def __str__(self):
        """
        Fornece uma representação do tipo String (como Matriz de Adjacência contendo Pesos) do grafo.
        :return: Uma string que representa o grafo
        """
        # Dá o espaçamento inicial do canto da borda superior esquerda
        grafo_str = ' ' * self.__maior_vertice

        # Dá o espaçamento correto entre os nomes dos vértices no cabeçalho da matriz
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
