from unittest import TestCase
from pingpong import PingPong

class PingPongTest(TestCase):

    def test_deve_imprimir_um_numero(self):
        pp = PingPong()
        self.assertEqual(pp.imprime_saida(7),7)

    def test_deve_imprimir_ping(self):
        pp = PingPong()
        self.assertEqual(pp.imprime_saida(3),'ping')
        
    def test_deve_imprimir_pong(self):
        pp = PingPong()
        self.assertEqual(pp.imprime_saida(5),'pong')

    def test_deve_imprimir_pingpong(self):
        pp = PingPong()
        self.assertEqual(pp.imprime_saida(15),'ping pong')

    def test_deve_imprimir_lista(self):
        pp = PingPong()
        resultado = [1,2,'ping',4,'pong','ping',7,8,'ping','pong',
            11,'ping',13,14,'ping pong']

        resposta = pp.gerar_lista(15)
        self.assertEqual(resposta,resultado)
