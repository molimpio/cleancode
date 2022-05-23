import unittest

from src.domain.entity.dimension import Dimension


class DimensionTestCase(unittest.TestCase):
    def test_deve_criar_coupon_desconto(self):
        dimension = Dimension(100, 30, 10)
        volume = dimension.get_volume()
        self.assertEqual(volume, 0.03)


if __name__ == '__main__':
    unittest.main()
