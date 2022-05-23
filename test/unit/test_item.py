import unittest

from src.domain.entity.dimension import Dimension
from src.domain.entity.item import Item


class ItemTestCase(unittest.TestCase):
    def test_deve_criar_um_item_com_dimensoes_e_calcular_volume(self):
        item = Item(1, 'Instrumentos musicais', 'Guitarra', 1000, Dimension(100, 30, 10))
        volume = item.get_volume()
        self.assertEqual(volume, 0.03)

    def test_deve_criar_um_item_com_dimensoes_e_calcular_densidade(self):
        item = Item(1, 'Instrumentos musicais', 'Guitarra', 1000, Dimension(100, 30, 10), 3)
        densidade = item.get_density()
        self.assertEqual(densidade, 100)


if __name__ == '__main__':
    unittest.main()
