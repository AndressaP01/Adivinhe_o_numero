import unittest

from app.sorteio import Sorteio


class TestSorteio(unittest.TestCase):
    def test_sorteio(self):
        sorteio=Sorteio()
        sorteio.sortear(89)
        self.assertEqual(1,1)
    def test_sorteio2(self):
        sorteio=Sorteio()
        sorteio.sortear(90)
        self.assertEqual(1 ,0)

    def test_sorteio3(self):
        sorteio = Sorteio()
        sorteio.sortear(5)
        self.assertEqual(1, 0)

    def test_sorteio4(self):
        sorteio = Sorteio()
        sorteio.sortear(10)
        self.assertEqual(1, 0)

    def test_sorteio5(self):
        sorteio = Sorteio()
        sorteio.sortear(1000)
        self.assertEqual(1, 0)

    def test_sorteio6(self):
        sorteio = Sorteio()
        sorteio.sortear(250)
        self.assertEqual(1, 0)

    def test_sorteio7(self):
        sorteio = Sorteio()
        sorteio.sortear(91)
        self.assertEqual(1, 0)

    def test_sorteio8(self):
        sorteio = Sorteio()
        sorteio.sortear(900)
        self.assertEqual(1, 0)

    def test_sorteio9(self):
        sorteio = Sorteio()
        sorteio.sortear(9000000)
        self.assertEqual(1, 0)

    def test_sorteio2(self):
        sorteio = Sorteio()
        sorteio.sortear(600000)
        self.assertEqual(1, 0)

