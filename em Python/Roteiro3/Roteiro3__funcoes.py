class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=None, A=None):
        """
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param A: Uma dicionário que guarda as grafo do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        """
        if A is None:
            A = {}
        if N is None:
            N = []

        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

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

        # Verifica se as grafo antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        """
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        """
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        """
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        """
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        """
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        """
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        """
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        """
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        """
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param nome: O nome da aresta a ser adicionada
        :param a: Os vértices que a aresta interliga separados pelo separador de arestas
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        """
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    '''
    - Soluções do Roteiro 3, Inicio -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    def __ciclo_aux(self):
        """
        Função auxiliar de ha_ciclo, semelhante a função de busca de caminho entre dois vértices, que encerra ao
        encontrar um laço no grafo.
        :return:
        """
        grafo = self.A.items()  # Dicionário do grafo contendo a aresta como chave e a ligação de vértices como valor
        lista_de_vertices = self.N  # Lista de vértices do grafo

        import random  # Biblioteca auxiliar que irá definir o vértice a ser usado como raiz inicialmente

        caminho = []  # Lista final contendo um caminho que possui um laço
        vertices_proibidos = []  # Lista com os vértices na qual a busca deve desconsiderar
        arestas_proibidas = []  # Lista com as arestas na qual a busca deve desconsiderar
        vertice_a_ser_buscado = random.choice(lista_de_vertices)  # Vértice a ser buscado
        while True:
            encontrou = False  # Variável auxiliar que indica se irá buscar o vertice_a_ser_buscado no segundo loop

            for item in grafo:
                aresta = item[0]
                vertice1 = item[1][0]
                vertice2 = item[1][2]
                if vertice1 == vertice_a_ser_buscado:
                    if vertice1 not in caminho and vertice1 not in vertices_proibidos:
                        caminho.append(vertice1)
                    if aresta not in caminho and aresta not in arestas_proibidas:
                        caminho.append(aresta)
                        if vertice2 not in caminho and vertice2 not in vertices_proibidos:
                            caminho.append(vertice2)
                            vertice_a_ser_buscado = vertice2
                            encontrou = True
                            break
                        else:
                            caminho.append(vertice2)
                            return caminho

            if not encontrou:
                for item in grafo:
                    aresta = item[0]
                    vertice1 = item[1][0]
                    vertice2 = item[1][2]
                    if vertice2 == vertice_a_ser_buscado:
                        if vertice2 not in caminho and vertice2 not in vertices_proibidos:
                            caminho.append(vertice2)
                        if aresta not in caminho and aresta not in arestas_proibidas:
                            caminho.append(aresta)
                            if vertice1 not in caminho and vertice1 not in vertices_proibidos:
                                caminho.append(vertice1)
                                vertice_a_ser_buscado = vertice1
                                encontrou = True
                                break
                            else:
                                caminho.append(vertice1)
                                return caminho

            if not encontrou:
                if len(caminho) > 1:
                    vertices_proibidos.append(caminho.pop())
                    arestas_proibidas.append(caminho.pop())
                    vertice_a_ser_buscado = caminho[-1]
                else:
                    return False

    def ha_ciclo(self):

        """
        Verifica se há um ciclo no objeto grafo.
        :return: Uma lista com a sequência de vértices e arestas do ciclo, caso houver, ou False caso contrário.
        """

        ha_ciclo = self.__ciclo_aux()  # Variável que vai guardar: ou uma Lista com o ciclo ou False
        caminho_ciclo = []  # Sequência de vértices e arestas do ciclo
        inicio_do_ciclo = False  # Marcador de início do ciclo na lista ha_ciclo
        if ha_ciclo:  # Se a variável ha_ciclo não estiver com valor falso e sim com a lista contendo o ciclo...
            for item in ha_ciclo:  # Percorre os items da lista em busca do primeiro elemento parecido com o último
                if item == ha_ciclo[-1]:  # Ao encontrar...
                    inicio_do_ciclo = True  # Marca como o Início do Ciclo
                if inicio_do_ciclo:
                    # E então começa adicionar os elementos a lista do caminho do ciclo
                    caminho_ciclo.append(item)
            return caminho_ciclo  # e retorna o caminho
        return False  # Caso a função ciclo_aux retorne falso, armazena falso na variável ha_ciclo

    def caminho_dois_vertices(self, x, y):

        """
        Função que verifica se há um caminho entre dois vértices.
        :param x: Vértice 1.
        :param y: Vértice 2.
        :return: Valor booleano. True se há, False caso contrário.
        """

        grafo = self.A.items()  # Dicionário do grafo contendo a aresta como chave e a ligação de vértices como valor
        lista_de_vertices = self.N  # Lista de vértices do grafo

        # Verifica se algum dos vértices do parâmetro existe
        if x not in lista_de_vertices or y not in lista_de_vertices:
            return False  # Caso não, sai da função e retorna False

        caminho = []  # Lista com o caminho entre os dois vértices
        vertices_proibidos = []  # Lista com os vértices na qual a busca deve desconsiderar
        arestas_proibidas = []  # Lista com as arestas na qual a busca deve desconsiderar
        vertice_a_ser_buscado = x  # Vértice a ser buscado
        while True:
            if len(caminho) > 0 and caminho[0] == x and caminho[-1] == y:
                # Se a lista contendo o caminho não estiver vazia e o primeiro elemento dela for igual ao x do parâmetro
                # e o último for igual ao y do parâmetro...
                return caminho
                # return True  # retorna True pois encontrou um caminho entre os dois.

            else:  # Caso contrário, continua a busca pois ainda não encontrou um caminho entre os dois

                encontrou = False  # Variável auxiliar que indica se irá buscar o vertice_a_ser_buscado no segundo loop

                # A primeira busca ocorre neste loop, verificando se encontra o vertice_a_ser_buscado nos vértices 1
                for item in grafo:
                    aresta = item[0]
                    vertice1 = item[1][0]
                    vertice2 = item[1][2]
                    if vertice1 == vertice_a_ser_buscado:
                        if vertice1 not in caminho and vertice1 not in vertices_proibidos:
                            caminho.append(vertice1)
                        if aresta not in caminho and aresta not in arestas_proibidas:
                            caminho.append(aresta)
                            if vertice2 not in caminho and vertice2 not in vertices_proibidos:
                                caminho.append(vertice2)
                                vertice_a_ser_buscado = vertice2
                                encontrou = True
                                break
                            else:
                                arestas_proibidas.append(caminho.pop())

                if not encontrou:
                    # Caso o vértice não seja encontrado no primeiro loop e a variável auxiliar ainda estiver com valor
                    # falso, busca neste segundo loop verificando os vértices 2
                    for item in grafo:
                        aresta = item[0]
                        vertice1 = item[1][0]
                        vertice2 = item[1][2]
                        if vertice2 == vertice_a_ser_buscado:
                            if vertice2 not in caminho and vertice2 not in vertices_proibidos:
                                caminho.append(vertice2)
                            if aresta not in caminho and aresta not in arestas_proibidas:
                                caminho.append(aresta)
                                if vertice1 not in caminho and vertice1 not in vertices_proibidos:
                                    caminho.append(vertice1)
                                    vertice_a_ser_buscado = vertice1
                                    encontrou = True
                                    break
                                else:
                                    arestas_proibidas.append(caminho.pop())

                # Se por acaso nenhum dos dois loops encontrar o vértice a ser buscado é porque este caminho não é
                # viável, então...
                if not encontrou:

                    # Caso o caminho seja maior que 2 elementos...
                    if len(caminho) > 1:
                        # Adiciona o último vértice e a última aresta encontrados na lista de proibidos,
                        vertices_proibidos.append(caminho.pop())
                        arestas_proibidas.append(caminho.pop())
                        vertice_a_ser_buscado = caminho[-1]
                        # e inicia a busca no penúltimo vértice encontrado, porém, em um caminho diferente, já que
                        # as listas de vértices e arestas proibidos foram atualizadas.

                    # Caso todos os caminhos_entre_dois_vertices possiveis entre os dois vertices tenham sido buscados e as listas de
                    # proibidos estejam cheias, é porque não existe caminho entre os dois, então...
                    else:
                        return False  # Retorna False

    def caminho(self, n):

        """
        Verifica se há um caminho de tamanho n no objeto grafo.
        :param n: Comprimento do caminho a ser buscado.
        :return: Uma lista com a sequência de vértices e arestas do caminho encontrado.
        """

        lista_de_vertices = self.N  # Lista de vértices do grafo

        # Loop que verifica o tamanho entre todos os vértices do grafo e compara com o tamanho n do parâmetro.
        for vertice1 in lista_de_vertices:
            for vertice2 in lista_de_vertices:
                caminho = self.caminho_dois_vertices(vertice1, vertice2)
                # Se por acaso existir um caminho de tamanho...
                if n * 2 + 1 == len(caminho):
                    return caminho  # retorna-o
        return False  # Ou falso caso contrário.

    def conexo(self):

        """
        Verifica se o objeto grafo é conexo.
        :return: Valor Booleano. True se for, False se não for.
        """

        lista_de_vertices = self.N

        # Verifica se há um caminho entre quaisquer dois vértices do grafo.
        for vertice1 in lista_de_vertices:
            for vertice2 in lista_de_vertices:
                if not self.caminho_dois_vertices(vertice1, vertice2):
                    return False  # Caso não exista um caminho entre dois dos vértices, retorna falso
        return True  # Caso termine o loop com sucesso, retorna verdadeiro

    '''
    - Soluções do Roteiro 3, Fim -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    # ---

    '''
    - Solução do Roteiro 2, Inicio -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    def __DFS_Auxiliar(self, vertice, verificados):

        """
        Função auxiliar à DFS que percorre o grafo recursivamente verificando se os vértices e arestas vizinhos_do_vertice já foram
        verificados, e em caso negativo, adicionando-os a lista de retorno, que representa a árvore DFS.
        :param vertice: O vértice a ser verificado.
        :param verificados: A lista que representa a árvore DFS que será retornada pela função principal.
        :return: Uma lista representando a árvore DFS.
        """

        for g in self.A.items():

            # g = ('a1', 'X-Y')
            # g[0] = aresta ('a1')
            # g[1] = vertices ('X-Y')
            # g[1][0] = vertice 1
            # g[1][2] = vertice 2

            # Se o vértice do parâmetro for igual ao vértice 1...
            if g[1][0] == vertice:
                # Se o vértice atual (do parâmetro / vértice 1) ainda não foi verificado...
                if g[1][0] not in verificados:
                    # Adiciona-o a lista de verificados.
                    verificados.append(g[1][0])

                # Se o vértice vizinho (conectado à ele) ainda não foi verificado...
                if g[1][2] not in verificados:
                    # Adiciona a aresta e ele à lista de verificados...
                    verificados.append(g[0])
                    verificados.append(g[1][2])
                    # e percorre o grafo recursivamente em busca das instâncias deste mesmo vértice na "posição 1".
                    self.__DFS_Auxiliar(g[1][2], verificados)

            # Se o vértice do parâmetro for igual ao vértice 2...
            elif g[1][2] == vertice:
                # Se o vértice atual (do parâmetro / vértice 2) ainda não foi verificado...
                if g[1][2] not in verificados:
                    # Adiciona-o a lista de verificados.
                    verificados.append(g[1][2])

                # Se o vértice vizinho (conectado à ele) ainda não foi verificado...
                if g[1][0] not in verificados:
                    # Adiciona a aresta e ele à lista de verificados...
                    verificados.append(g[0])
                    verificados.append(g[1][0])
                    # e percorre o grafo recursivamente em busca das instâncias deste mesmo vértice na "posição 1".
                    self.__DFS_Auxiliar(g[1][0], verificados)

        return verificados

    def DFS(self, vertice_raiz):

        """
        Função DFS principal que retorna uma Árvore DFS do Grafo/objeto.
        :param vertice_raiz: Vértice/raiz. Ponto de partida da busca.
        :return: Uma lista representando a Árvore DFS do Grafo.
        """

        # Retorna o resultado da função auxiliar recursiva, onde é passado como argumento:
        # o Vértice Raiz e uma Lista vazia que será a Árvore DFS retornada.
        return self.__DFS_Auxiliar(vertice_raiz, [])

    '''
    - Solução do Roteiro 2, Fim -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    # ---

    '''
    - Soluções do Roteiro 1, Inicio -
    (Copyright © Guilherme Esdras 2019.2)
    '''

    # 2-a) Encontre todos os pares de vértices não adjacentes.
    def vertices_nao_adjacentes(self):

        """
        Armazena todos os vértices não adjacentes (que "não estão conectados") de um grafo em uma lista.
        :return: Uma lista com todos os vértices não adjacentes do objeto/grafo.
        """

        # Valores/grafo do dicionário de arestas do objeto/grafo
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

        """
        Verifica se há algum laço no grafo.
        :return: Valor booleano. True caso houver ou False caso contrário.
        """

        lista_de_arestas = self.A.values()

        # Para cada um dos conjuntos de vértices (valores) da lista de arestas do objeto/grafo (dicionário)...
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

        """
        Verifica se há grafo paralelas (duas grafo partindo do mesmo vértice para outro vértice) no grafo.
        :return: Valor booleano. True caso houver ou False caso contrário.
        """

        # Variáveis iniciais
        lista_de_arestas = self.A.values()
        sep = self.SEPARADOR_ARESTA

        # Listas que armazenam as arestas verificadas.
        arestas_indo_verificadas = []
        arestas_vindo_verificadas = []

        # Para cada aresta na lista de arestas do objeto/grafo...
        for aresta in lista_de_arestas:

            # aresta[x] == 'XXX' (caracter X do valor/aresta)

            # Guarda a aresta em sentidos diferentes...
            aresta_indo = '{}{}{}'.format(aresta[0], sep, aresta[2])
            aresta_vindo = '{}{}{}'.format(aresta[2], sep, aresta[0])

            # Se esta aresta já está em uma das listas de verificadas...
            if (aresta_indo in arestas_indo_verificadas) or (aresta_vindo in arestas_vindo_verificadas):
                # é porque o grafo em questão possui duas arestas partindo do mesmo vértice, então...
                return True  # é paralela.

            # Caso contrário...
            else:
                # Adiciona as arestas nas listas de verificadas.
                arestas_indo_verificadas.append(aresta_indo)
                arestas_vindo_verificadas.append(aresta_vindo)

        # Caso o loop não encontre duas arestas...
        return False  # não possui paralelas.

    # 2-v2) Qual o grau de um vértice arbitrário?
    def grau(self, v):

        """
        Verifica o grau de um determinado vértice (passado como argumento desta função) do objeto grafo.
        :param v: Vértice na qual procura-se o grau.
        :return: Valor Inteiro, indicando o grau do vértice do parâmetro.
        """

        # Variável que armazena a lista de grafo&vértices do grafo/objeto
        lista_de_arestas = self.A.values()

        # Variável contador auxiliar que armazenará o grau do vértice verticeParam
        grau = 0

        # Para cada um dos conjuntos de vértices (valores) da lista de arestas do objeto/grafo (dicionário)...
        for vertice in lista_de_arestas:

            # vertice[x] == 'XXX' (Caracter X do valor/aresta)
            # Ex.: vertice[0] == vértice 1 / vertice[1] == separador / vertice[2] == vértice 2

            # Se um dos vértices for igual ao vértice do parâmetro...
            if (vertice[0] == v) or (vertice[2] == v):
                # Incrementa o "contador de grau"
                grau += 1

        # Retorna o grau do vértice verticeParam
        return grau

    # 2-e) Quais arestas incidem sobre um vértice N arbitrário?
    def arestas_sobre_vertice(self, vertice):

        """
        Verifica todas as arestas que incidem sobre o vértice passado como argumento da função
        :param vertice: Vértice em questão
        :return: Uma lista com todas as arestas
        """

        # Lista que armazena as arestas
        lista_de_arestas = []

        # Para cada aresta no Dicionário de arestas do grafo...
        for aresta in self.A.items():

            # aresta[0] == 'a1'... (chave do dicionário)
            # aresta[1] == 'V1-V2'... (valor do dicionário)
            # aresta[1][x] == 'XXX'... (caracter do valor do dicionário)

            # Se um dos vértices for igual ao vértice do parâmetro...
            if aresta[1][0] == vertice or aresta[1][2] == vertice:

                # Adiciona a aresta em questão a lista de arestas.
                lista_de_arestas.append(aresta[0])

        # Retorna a lista de arestas
        return lista_de_arestas

    # 2-f) Esse grafo é completo?
    def eh_completo(self):

        """
        Verifica se o grafo objeto é completo, analisando as combinações de arestas.
        :return: Valor Booleano. True se for verdadeiro, ou False caso contrário.
        """

        # Variáveis iniciais
        lista_de_vertices = self.N
        lista_de_arestas = self.A.values()

        n = len(lista_de_vertices)

        if n == 1:
            return True

        # Quantidade máxima de arestas permitidas em um grafo completo
        max_de_arestas = (n * (n - 1)) // 2

        # Lista que armazenará as arestas verificadas
        arestas_verificadas = []

        # Para cada par de vértice na lista de arestas...
        for vertice in lista_de_arestas:

            # vertice[x] == 'XXX' (Caracter X do valor/aresta)
            # Ex.: vertice[0] == vértice 1 / vertice[2] == vértice 2

            # if vertice[0] == vertice[2]:
            #     return False

            # analisa o vértice voltando...
            vertice_contrario = '{}{}{}'.format(vertice[2], vertice[1], vertice[0])

            # se por acaso o par de vértice já tiver sido verificado...
            if (vertice in arestas_verificadas) or (vertice_contrario in arestas_verificadas):
                return False  # Retorna falso, pois grafos completos não possuem arestas paralelas

            # caso contrário, adiciona na lista de verificadas.
            else:
                arestas_verificadas.append(vertice)

        # Se sair do loop, verifica se a quantidade de arestas verificadas está de acordo com a quantidade permitida
        if len(arestas_verificadas) == max_de_arestas or len(arestas_verificadas) == 2:
            return True  # Se sim, é um grafo completo, retorna True

        # Se por algum motivo não bater...
        else:
            return False  # Retorna False

    '''
    - Soluções do Roteiro 1, Fim -
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
