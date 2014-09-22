from unittest import TestCase
from jokenpo import Jokenpo

class JokenpoTest(TestCase):

    def test_jogada_empate(self):
        j = Jokenpo()
        esperado = 'empate'
        resposta = j.jogada('pedra', 'pedra')
        self.assertEqual(resposta, esperado)

    def test_jogada_pedra_ganha(self):
        j = Jokenpo()
        esperado = 'pedra_ganha'
        resposta = j.jogada('pedra', 'tesoura')
        self.assertEqual(resposta, esperado)

    def test_jogada_tesoura_ganha(self):
        j = Jokenpo()
        esperado = 'tesoura_ganha'
        resposta = j.jogada('tesoura', 'papel')
        self.assertEqual(resposta, esperado)

    def test_jogada_papel_ganha(self):
        j = Jokenpo()
        esperado = 'papel_ganha'
        resposta = j.jogada('papel', 'pedra')
        self.assertEqual(resposta, esperado)
    
