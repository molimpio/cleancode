import unittest

import pytest

from datetime import datetime
from src.domain.entity.dimension import Dimension
from src.domain.entity.item import Item
from src.domain.entity.coupon import Coupon
from src.domain.entity.order import Order


class ItemTestCase(unittest.TestCase):
    def test_nao_deve_criar_pedido_com_cpf_invalido(self):
        with pytest.raises(Exception) as e:
            Order('111.111.111-11')
        self.assertEqual(str(e.value), 'CPF inválido')

    def test_deve_criar_um_pedido_com_tres_itens(self):
        order = Order('935.411.347-80')
        order.add_item(Item(1, 'Instrumentos musicais', 'Guitarra', 1000), 1)
        order.add_item(Item(2, 'Instrumentos musicais', 'Amplificador', 5000), 1)
        order.add_item(Item(3, 'Instrumentos musicais', 'Cabo', 30), 3)
        total = order.get_total()
        self.assertEqual(total, 6090)

    def test_deve_criar_um_pedido_calculando_codigo(self):
        order = Order('935.411.347-80', datetime(2021, 10, 10), 1)
        order.add_item(Item(1, 'Instrumentos musicais', 'Guitarra', 1000), 1)
        order.add_item(Item(2, 'Instrumentos musicais', 'Amplificador', 5000), 1)
        order.add_item(Item(3, 'Instrumentos musicais', 'Cabo', 30), 3)
        self.assertEqual(order.code.value, '202100000001')

    def test_deve_criar_um_pedido_com_tres_itens_com_cupom_desconto(self):
        order = Order('935.411.347-80')
        order.add_item(Item(1, 'Instrumentos musicais', 'Guitarra', 1000), 1)
        order.add_item(Item(2, 'Instrumentos musicais', 'Amplificador', 5000), 1)
        order.add_item(Item(3, 'Instrumentos musicais', 'Cabo', 30), 3)
        coupon = Coupon('VALE20', 20)
        order.add_coupon(coupon)
        total = order.get_total()
        self.assertEqual(total, 4872)

    def test_deve_criar_um_pedido_com_tres_itens_com_cupom_desconto_expirado(self):
        order = Order('935.411.347-80')
        order.add_item(Item(1, 'Instrumentos musicais', 'Guitarra', 1000), 1)
        order.add_item(Item(2, 'Instrumentos musicais', 'Amplificador', 5000), 1)
        order.add_item(Item(3, 'Instrumentos musicais', 'Cabo', 30), 3)
        coupon = Coupon('VALE20', 20, datetime(2021, 10, 10))
        order.add_coupon(coupon)
        total = order.get_total()
        self.assertEqual(total, 6090)

    def test_deve_criar_um_pedido_com_tres_itens_e_calcular_frete(self):
        order = Order('935.411.347-80')
        order.add_item(Item(1, 'Instrumentos musicais', 'Guitarra', 1000, Dimension(100, 30, 10), 3), 1)
        order.add_item(Item(2, 'Instrumentos musicais', 'Amplificador', 5000, Dimension(100, 50, 50), 20), 1)
        order.add_item(Item(3, 'Instrumentos musicais', 'Cabo', 30, Dimension(10, 10, 10), 1), 3)
        total = order.get_total()
        self.assertEqual(total, 6350)

    def test_deve_criar_um_pedido_com_um_item_e_calcular_frete_minimo(self):
        order = Order('935.411.347-80')
        order.add_item(Item(3, 'Instrumentos musicais', 'Cabo', 30, Dimension(10, 10, 10), 0.9), 1)
        total = order.get_total()
        self.assertEqual(total, 40)


if __name__ == '__main__':
    unittest.main()
