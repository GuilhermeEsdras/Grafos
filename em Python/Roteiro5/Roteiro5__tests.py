import unittest
from Roteiro5__funcoes import Grafo


class TestEuler(unittest.TestCase):

    def setUp(self):

        # Pontes de Konigsberg
        self.konigsberg = Grafo([], [])
        for i in ['M', 'T', 'B', 'R']:
            self.konigsberg.adicionaVertice(i)
        for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
            self.konigsberg.adicionaAresta(i)

        # Grafos com caminho euleriano
        self.konigsberg_mod = Grafo([], [])
        for i in ['M', 'T', 'B', 'R']:
            self.konigsberg_mod.adicionaVertice(i)
        for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
            self.konigsberg_mod.adicionaAresta(i)

        self.g_c_e = Grafo([], [])
        for i in ['A', 'B', 'C']:
            self.g_c_e.adicionaVertice(i)
        for i in ['A-B', 'B-C']:
            self.g_c_e.adicionaAresta(i)

        # GrafoComPesos da Paraíba
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adicionaVertice(i)
        for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p.adicionaAresta(i)

        # GrafoComPesos da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p_sem_paralelas.adicionaVertice(i)
        for i in ['J-C', 'C-E', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
            self.g_p_sem_paralelas.adicionaAresta(i)

        # Grafos completos
        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adicionaVertice(i)
        for i in ['J-C', 'J-E', 'J-P', 'C-E', 'C-P', 'E-P']:
            self.g_c.adicionaAresta(i)

        self.g_c2 = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c2.adicionaVertice(i)
        for i in ['J-C', 'E-J', 'J-P', 'E-C', 'C-P', 'P-E']:
            self.g_c2.adicionaAresta(i)

        self.g_c3 = Grafo([], [])
        self.g_c3.adicionaVertice('J')

        # Grafos com laco
        self.g_l1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l1.adicionaVertice(i)
        for i in ['A-A', 'B-A', 'A-A']:
            self.g_l1.adicionaAresta(i)

        self.g_l2 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l2.adicionaVertice(i)
        for i in ['A-B', 'B-B', 'B-A']:
            self.g_l2.adicionaAresta(i)

        self.g_l3 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D']:
            self.g_l3.adicionaVertice(i)
        for i in ['C-A', 'C-C', 'D-D']:
            self.g_l3.adicionaAresta(i)

        self.g_l4 = Grafo([], [])
        self.g_l4.adicionaVertice('D')
        self.g_l4.adicionaAresta('D-D')

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adicionaVertice(i)
        for i in ['D-C', 'C-C']:
            self.g_l5.adicionaAresta(i)

    def test_possui_caminho_euleriano(self):
        self.assertTrue(self.konigsberg_mod.possui_caminho_euleriano())
        self.assertTrue(self.g_c_e.possui_caminho_euleriano())
        self.assertTrue(self.g_c_e.possui_caminho_euleriano())

        self.assertFalse(self.konigsberg.possui_caminho_euleriano())
        self.assertFalse(self.g_p.possui_caminho_euleriano())
        self.assertFalse(self.g_p_sem_paralelas.possui_caminho_euleriano())
        self.assertFalse(self.g_c.possui_caminho_euleriano())
