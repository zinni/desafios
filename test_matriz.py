from unittest import TestCase

class TestMatriz(TestCase):


    def test_matriz_0x0(self):
        esperado = 0
        resposta = matriz[0][0]
        self.assertEqual(resposta, esperado)

    def test_matriz_5x5(self):
        esperado = 0
        resposta = matriz[5][5]
        self.assertEqual(resposta, esperado)
