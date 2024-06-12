import unittest
from city_functions import cities


class TestCity(unittest.TestCase):
    def test(self):
        cidadePais = cities("Santiago", "Chile", 50000000)
        self.assertEqual(cidadePais, 'Santiago, Chile - populacao: 50000000')

    unittest.main()


print(TestCity())
