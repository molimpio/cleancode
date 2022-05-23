import unittest
from datetime import datetime
from src.domain.entity.order_code import OrderCode


class OrderCodeTestCase(unittest.TestCase):
    def test_deve_criar_codigo_pedido(self):
        date = datetime(2021, 3, 1)
        sequence = 1
        order_code = OrderCode(date, sequence)
        code = order_code.value
        self.assertEqual(code, '202100000001')


if __name__ == '__main__':
    unittest.main()
