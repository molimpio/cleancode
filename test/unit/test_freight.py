import unittest

from src.domain.entity.dimension import Dimension
from src.domain.entity.freight import Freight
from src.domain.entity.item import Item


class FreightTestCase(unittest.TestCase):
    def test_deve_calcular_frete_de_um_item(self):
        item = Item(1, 'Instrumentos musicais', 'Guitarra', 1000, Dimension(100, 30, 10), 3)
        freight = Freight()
        freight.add_item(item, 2)
        self.assertEqual(60, freight.get_total())

    def test_deve_calcular_frete_minimo_de_um_item(self):
        item = Item(3, 'Instrumentos musicais', 'Cabo', 30, Dimension(10, 10, 10), 0.9)
        freight = Freight()
        freight.add_item(item, 1)
        self.assertEqual(10, freight.get_total())


if __name__ == '__main__':
    unittest.main()
