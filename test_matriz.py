from unittest import TestCase
from matriz import Matriz

class TestMatriz(TestCase):


    def test_matriz_0x0(self):
        matriz = Matriz()
        esperado = 1
        resposta = matriz.matrix()[0][0] 
        self.assertEqual(resposta, esperado)

    def test_matriz_5x5(self):
        matriz = Matriz()
        esperado = 1
        resposta = matriz.matrix()[5][5]
        self.assertEqual(resposta, esperado)

    def test_matriz_1x2(self):
        matriz = Matriz()
        esperado = 0
        resposta = matriz.matrix()[1][2]
        self.assertEqual(resposta, esperado)

    def test_matriz_9x8(self):
        matriz = Matriz()
        esperado = 0
        resposta = matriz.matrix()[9][8]
        self.assertEqual(resposta, esperado)
