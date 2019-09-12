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
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k>l:
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
                if i>j and not(M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not(self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-') # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
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
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
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

    #2 questao letra a
    def vertices_nao_adjacentes(self):
       lista = []
       for x in range(len(self.N)):
           for y in range(len(self.N)):
               aresta = '{}-{}'.format(self.N[x], self.N[y])
               if self.M[x][y] != '-' and self.M[x][y] == 0:
                   lista.append(aresta)
       return lista

    #2 questao letra b
    def ha_laco(self):
       contador = 0
       for x in self.M:
           if x[contador] >= 1:
               return True
           contador += 1
       return False

    #2 questao letra c
    def ha_paralelas(self):
       for x in range(len(self.N)):
           for y in range(len(self.N)):
               if self.M[x][y] != '-' and self.M[x][y] >= 2:
                   return True
       return False

    #2 questao letra d
    def grau(self, vertice):
       somador = 0
       for x in range(len(self.N)):
           if self.N[x] == vertice:
               for y in range(len(self.N)):
                   if self.M[x][y] != '-':
                       somador += self.M[x][y]
                   elif self.M[y][x] != '-':
                       somador += self.M[y][x]
       return somador

    #2 questao letra e
    def arestas_sobre_vertice(self, vertice):
       lista = []
       for x in range(len(self.N)):
           if self.N[x] == vertice:
               for y in range(len(self.N)):
                   aresta = '{}-{}'.format(self.N[x], self.N[y])
                   aresta1 = '{}-{}'.format(self.N[y], self.N[x])
                   if self.M[x][y] != '-' and self.M[x][y] > 0:
                       if self.M[x][y] != '-' and self.M[x][y] > 1:
                           for z in range(self.M[x][y]):
                               lista.append(aresta)
                       else:
                           lista.append(aresta)
                   elif self.M[y][x] != '-' and self.M[y][x] > 0:
                       if self.M[y][x] != '-' and self.M[y][x] > 1:
                           for z in range(self.M[y][x]):
                               lista.append(aresta1)
                       else:
                           lista.append(aresta1)
       return lista

    #2 questao letra f
    def eh_completo(self):
       for x in range(len(self.N)):
           for y in range(len(self.N)):
               if self.M[x][y] != '-' and x != y and self.M[x][y] == 0:
                   return False
       return True

    #2 questao letra g
    def ha_ciclo(self):
       contador = 0
       listpostion=[]
       new_x=0
       vertices=self.N
       listvertices=[]
       for x in range(len(self.M)):
            for y in range(len(self.M[x])):
                y+=1
                try:

                    posicao = self.M[x][y]
                    new_vertice = str(vertices[x]) + "-" + str(vertices[y])

                    if posicao!= "-" and posicao>=1 :
                        listpostion.append(posicao)
                        listvertices.append(new_vertice)
                        new_x=x
                        if new_x>=1:
                            new_x=0
                            while new_x != x:

                                new_position = self.M[new_x][y]
                                new_vertice = str(vertices[new_x]) + "-" + str(vertices[y])
                                if new_position>=1:
                                    listpostion.append(new_position)
                                    listvertices.append(new_vertice)
                                    return listvertices
                                new_x+=1
                    else:
                        listvertices.clear()

                except IndexError:
                    pass
                x+=1
                contador += 1

       return False


    #2 questao letra h
    def comprimento_de_tamanho_n(self, n, vertice=None, visitado=[], caminho=[], bordas=None, contador=0):
        if vertice == None:
            vertice = self.N[0]
        if bordas == None:
            bordas = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] != '-' and self.M[i][j] > 0:
                        for k in range(self.M[i][j]):
                            bordas.append(self.N[i] + "-" + self.N[j])
        if vertice in visitado:
            return False
        else:
            contador += 1
            if contador == n:
                return True
            visitado.append(vertice)
            bordas_adjacentes = self.arestas_sobre_vertice(vertice)
            for i in bordas_adjacentes:
                if i in bordas:
                    bordas.remove(i)
                proximo = i.split("-")
                if proximo[0] == vertice:
                    caminho.append(vertice + "-" + proximo[1])
                    result = self.comprimento_de_tamanho_n(n, proximo[1], visitado, caminho, bordas, contador)
                    if result:
                        return True
                    else:
                        caminho.pop()
                        contador -= 1
                else:
                    if len(bordas_adjacentes) != 1:
                        caminho.append(vertice + "-" + proximo[0])
                        result = self.comprimento_de_tamanho_n(n, proximo[0], visitado, caminho, bordas, contador)
                        if result:
                            return True
                        else:
                            caminho.pop()
                            contador -= 1
        return False

    #2 questao letra i
    def eh_conexo(self, vertice=None, visitado=[], caminho=[], bordas=None):
        if vertice is None:
            vertice = self.N[0]
        if bordas is None:
            bordas = []
            for i in range(len(self.N)):
                for j in range(len(self.N)):
                    if self.M[i][j] != '-' and self.M[i][j] > 0:
                        for k in range(self.M[i][j]):
                            bordas.append(self.N[i] + "-" + self.N[j])
        if vertice in visitado:
            if len(visitado) == len(self.N):
                return True
            else:
                return False
        else:
            visitado.append(vertice)
            bordas_adjacentes = self.arestas_sobre_vertice(vertice)
            for i in bordas_adjacentes:
                proximo = i.split("-")
                if proximo[0] == vertice:
                    caminho.append(vertice + "-" + proximo[1])
                    if self.eh_conexo(proximo[1], visitado, caminho, bordas):
                        return True
                    else:
                        caminho.pop()
                else:
                    if len(bordas_adjacentes) != 1:
                        caminho.append(vertice + "-" + proximo[0])
                        if self.eh_conexo(proximo[0], visitado, caminho, bordas):
                            return True
                        else:
                            caminho.pop()
        return False






    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

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































