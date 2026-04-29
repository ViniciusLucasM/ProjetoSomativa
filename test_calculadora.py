import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
    # Teste 1
    def test_soma(self):
        self.assertEqual(soma(10, 5), 15)

    # Teste 2
    def test_subtracao(self):
        self.assertEqual(subtracao(10, 5), 5)

    # Teste 3
    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(10, 5), 50)

    # Teste 4
    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)

    # Teste 5
    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divisao(10, 0)

if __name__ == '__main__':
    unittest.main()