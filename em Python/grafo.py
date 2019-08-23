class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as grafo do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

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

        # Verifica se as grafo antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    ###

    '''
    - Soluções do Roteiro 1, Inicio -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    # 2-a) Encontre todos os pares de vértices não adjacentes.
    def vertices_nao_adjacentes(self):

        '''
        Armazena todos os vértices não adjacentes (que "não estão conectados") de um grafo em uma lista.
        :return: Uma lista com todos os vértices não adjacentes do objeto/grafo.
        '''

        # Valores/grafo do dicionário de grafo do objeto/grafo
        lista_de_arestas = self.A.values()

        # Lista que armazenará os vértices não adjacentes
        lista_de_nao_adjacentes = []

        for v1 in self.N:
            for v2 in self.N:
                aresta_indo = '{}{}{}'.format(v1, self.SEPARADOR_ARESTA, v2)
                aresta_vindo = '{}{}{}'.format(v2, self.SEPARADOR_ARESTA, v1)
                if (aresta_indo not in lista_de_arestas) and (aresta_vindo not in lista_de_arestas):
                    lista_de_nao_adjacentes.append(aresta_indo)

        return lista_de_nao_adjacentes

    # 2-b) Há algum vértice adjacente a ele mesmo? (Retorne True ou False)
    def ha_laco(self):

        '''
        Verifica se há algum laço no grafo.
        :return: Valor booleano. True caso houver ou False caso contrário.
        '''

        lista_de_arestas = self.A.values()

        # Para cada um dos conjuntos de vértices (valores) da lista de grafo do objeto/grafo (dicionário)...
        for vertice in lista_de_arestas:

            # vertice[x] == 'XXX' (Caracter X do valor/aresta)
            # Ex.: vertice[0] == vértice 1 / vertice[1] == separador / vertice[2] == vértice 2

            # Se os vértices forem iguais...
            if vertice[0] == vertice[2]:
                return True  # É um laço

        # Caso saia do loop sem retornar nada...
        return False  # Não foram encontrados laços.

    # 2-c) Há grafo paralelas? (Retorne True ou False)
    def ha_paralelas(self):

        '''
        Verifica se há grafo paralelas (duas grafo partindo do mesmo vértice para outro vértice) no grafo.
        :return: Valor booleano. True caso houver ou False caso contrário.
        '''

        # Variáveis iniciais
        lista_de_arestas = self.A.values()
        sep = self.SEPARADOR_ARESTA

        # Listas que armazenam as grafo verificadas.
        arestas_indo_verificadas = []
        arestas_vindo_verificadas = []

        # Para cada aresta na lista de grafo do objeto/grafo...
        for aresta in lista_de_arestas:

            # aresta[x] == 'XXX' (caracter X do valor/aresta)

            # Guarda a aresta em sentidos diferentes...
            aresta_indo = '{}{}{}'.format(aresta[0], sep, aresta[2])
            aresta_vindo = '{}{}{}'.format(aresta[2], sep, aresta[0])

            # Se esta aresta já está em uma das listas de verificadas...
            if (aresta_indo in arestas_indo_verificadas) or (aresta_vindo in arestas_vindo_verificadas):
                # é porque o grafo em questão possui duas grafo partindo do mesmo vértice, então...
                return True  # é paralela.

            # Caso contrário...
            else:
                # Adiciona as grafo nas listas de verificadas.
                arestas_indo_verificadas.append(aresta_indo)
                arestas_vindo_verificadas.append(aresta_vindo)

        # Caso o loop não encontre duas grafo...
        return False  # não possui paralelas.

    # 2-d) Qual o grau de um vértice arbitrário?
    def grau(self, v):

        '''
        Verifica o grau de um determinado vértice (passado como argumento desta função) do objeto grafo.
        :param v: Vértice na qual procura-se o grau.
        :return: Valor Inteiro, indicando o grau do vértice do parâmetro.
        '''

        # Variável que armazena a lista de grafo&vértices do grafo/objeto
        lista_de_arestas = self.A.values()

        # Variável contador auxiliar que armazenará o grau do vértice v
        grau = 0

        # Para cada um dos conjuntos de vértices (valores) da lista de grafo do objeto/grafo (dicionário)...
        for vertice in lista_de_arestas:

            # vertice[x] == 'XXX' (Caracter X do valor/aresta)
            # Ex.: vertice[0] == vértice 1 / vertice[1] == separador / vertice[2] == vértice 2

            # Se um dos vértices for igual ao vértice do parâmetro...
            if (vertice[0] == v) or (vertice[2] == v):
                # Incrementa o "contador de grau"
                grau += 1

        # Retorna o grau do vértice v
        return grau

    # 2-e) Quais grafo incidem sobre um vértice N arbitrário?
    def arestas_sobre_vertice(self, vertice):

        '''
        Verifica todas as grafo que incidem sobre o vértice passado como argumento da função
        :param vertice: Vértice em questão
        :return: Uma lista com todas as grafo
        '''

        # Lista que armazena as grafo
        lista_de_arestas = []

        # Para cada aresta no Dicionário de grafo do grafo...
        for aresta in self.A.items():

            # aresta[0] == 'a1'... (chave do dicionário)
            # aresta[1] == 'V1-V2'... (valor do dicionário)
            # aresta[1][x] == 'XXX'... (caracter do valor do dicionário)

            # Se um dos vértices for igual ao vértice do parâmetro...
            if aresta[1][0] == vertice or aresta[1][2] == vertice:

                # Adiciona a aresta em questão a lista de grafo.
                lista_de_arestas.append(aresta[0])

        # Retorna a lista de grafo
        return lista_de_arestas

    # 2-f) Esse grafo é completo?
    def eh_completo(self):

        '''
        Verifica se o grafo objeto é completo, analisando as combinações de grafo.
        :return: Valor Booleano. True se for verdadeiro, ou False caso contrário.
        '''

        # Variáveis iniciais
        lista_de_vertices = self.N
        lista_de_arestas = self.A.values()

        n = len(lista_de_vertices)

        if n == 1:
            return True

        # Quantidade máxima de grafo permitidas em um grafo completo
        max_de_arestas = (n * (n - 1)) // 2

        # Lista que armazenará as grafo verificadas
        arestas_verificadas = []

        # Para cada par de vértice na lista de grafo...
        for vertice in lista_de_arestas:

            # vertice[x] == 'XXX' (Caracter X do valor/aresta)
            # Ex.: vertice[0] == vértice 1 / vertice[2] == vértice 2

            # if vertice[0] == vertice[2]:
            #     return False

            # analisa o vértice voltando...
            vertice_contrario = '{}{}{}'.format(vertice[2], vertice[1], vertice[0])

            # se por acaso o par de vértice já tiver sido verificado...
            if (vertice in arestas_verificadas) or (vertice_contrario in arestas_verificadas):
                return False  # Retorna falso, pois grafos completos não possuem grafo paralelas

            # caso contrário, adiciona na lista de verificadas.
            else:
                arestas_verificadas.append(vertice)

        # grau_dos_vertices = []
        #
        # for vertice in lista_de_vertices:
        #     grau_dos_vertices.append(str(self.grau(vertice)))
        #
        # if grau_dos_vertices.count(grau_dos_vertices[0]) != len(grau_dos_vertices):
        #     return False

        # Se sair do loop, verifica se a quantidade de grafo verificadas está de acordo com a quantidade permitida
        if len(arestas_verificadas) == max_de_arestas or len(arestas_verificadas) == 2:
            return True  # Se sim, é um grafo completo, retorna True

        # Se por algum motivo não bater...
        else:
            return False  # Retorna False

    '''
    - Soluções do Roteiro 1, Fim -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    # ---

    '''
    - Soluções do Roteiro 2, Inicio -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    # Em construção... ._.
    def __DFS_Auxiliar(self, grafo, vertice, verificados):
        for g in grafo:
            # g = ('a1', 'X-Y')
            # g[0] = aresta ('a1')
            # g[1] = vertices ('X-Y')
            # g[1][0] = vertice 1
            # g[1][2] = vertice 2
            if g[1][0] == vertice:
                if g[1][0] not in verificados:
                    verificados.append(g[1][0])
                if g[0] not in verificados:
                    verificados.append(g[0])
                if g[1][2] not in verificados:
                    verificados.append(g[1][2])
                    self.__DFS_Auxiliar(grafo, g[1][2], verificados)

        return verificados

    def DFS(self, v):
        grafo = self.A.items()
        return self.__DFS_Auxiliar(grafo, v, [])

    '''
    - Soluções do Roteiro 2, Fim -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das grafo no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str