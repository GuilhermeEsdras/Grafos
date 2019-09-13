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
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
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
                    vertices_nao_adjacentes.append('{}{}{}'.format(self.N[x], self.SEPARADOR_ARESTA, self.N[y]))
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

        pos = self.N.index(v)
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
                                qtd = 0
                                while qtd < arestas:
                                    vertices_incidentes.append(
                                        '{}{}{}'.format(self.N[x], self.SEPARADOR_ARESTA, self.N[y])
                                    )
                                    qtd += 1
                    else:
                        if arestas != '-':
                            if arestas > 0:
                                qtd = 0
                                while qtd < arestas:
                                    vertices_incidentes.append(
                                        '{}{}{}'.format(self.N[x], self.SEPARADOR_ARESTA, self.N[y])
                                    )
                                    qtd += 1
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
