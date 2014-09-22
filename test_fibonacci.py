from unittest import TestCase
from fibonacci import fibonacci

class TestFibonacci(TestCase):


    def test_fibonacci_um(self):
        esperado = 1
        resposta = fibonacci(1)
        self.assertEqual(resposta, esperado)

    def test_fibonacci_cinco(self):
        esperado = 5
        resposta = fibonacci(5)
        self.assertEqual(resposta, esperado)

    def test_fibonacci_dez(self):
        esperado = 55
        resposta = fibonacci(10)
        self.assertEqual(resposta, esperado)
