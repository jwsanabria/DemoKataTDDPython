from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora.sumar(self, " "), 0, "Cadena vacia")
