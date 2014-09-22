from unittest import TestCase
from segundograu import baskara

class TestBaskara(TestCase):
    
    def test_baskara_positivo(self):
        esperado = (-1.0, -3.0)
        resposta = baskara(1,4,3)
        self.assertEqual(resposta, esperado)

    def test_baskara_negativo(self):
        esperado = 'raiz irreal'
        resposta = baskara(15,2,45)
        self.assertEqual(resposta, esperado)

    def test_baskara_zero(self):
        esperado = -1.0
        resposta = baskara(1,2,1)
        self.assertEqual(resposta, esperado)
        
    def test_baskara_azero(self):
        esperado = 'a nao pode ser 0'
        resposta = baskara(0,4,3)
        self.assertEqual(resposta, esperado)
