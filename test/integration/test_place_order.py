import unittest
from datetime import datetime
from src.infra.repository.memory.coupon_repository_memory import CouponRepositoryMemory
from src.infra.repository.memory.item_repository_memory import ItemRepositoryMemory
from src.infra.repository.postgresql.item_repository_postgresql import ItemRepositoryPostgreSQL
from src.infra.repository.memory.order_repository_memory import OrderRepositoryMemory
from src.application.usecase.place_order.place_order import PlaceOrder
from src.application.usecase.place_order.place_order_input import PlaceOrderInput
from src.infra.database.postgre_sql_connection_adapter import PostgreSQLConnectionAdapter


class PlaceOrderTestCase(unittest.TestCase):

    def test_deve_fazer_um_pedido(self):
        connection = PostgreSQLConnectionAdapter()
        item_repository = ItemRepositoryPostgreSQL(connection)
        order_repository = OrderRepositoryMemory()
        coupon_repository = CouponRepositoryMemory()
        place_order = PlaceOrder(item_repository, order_repository, coupon_repository)

        order_itens = [
            {'id_item': 1, 'quantity': 1},
            {'id_item': 2, 'quantity': 1},
            {'id_item': 3, 'quantity': 3},
        ]

        place_order_input = PlaceOrderInput('935.411.347-80', order_itens, 'VALE20')

        output = place_order.execute(place_order_input)
        self.assertEqual(output.total, 5152)
        connection.close()

    def test_deve_fazer_um_pedido_calculando_codigo(self):
        item_repository = ItemRepositoryMemory()
        order_repository = OrderRepositoryMemory()
        coupon_repository = CouponRepositoryMemory()
        place_order = PlaceOrder(item_repository, order_repository, coupon_repository)

        order_itens = [
            {'id_item': 1, 'quantity': 1},
            {'id_item': 2, 'quantity': 1},
            {'id_item': 3, 'quantity': 3},
        ]

        date = datetime(2021, 10, 10)

        place_order_input = PlaceOrderInput('935.411.347-80', order_itens, 'VALE20', date)

        place_order.execute(place_order_input)
        output = place_order.execute(place_order_input)
        self.assertEqual(output.code, '202100000002')


if __name__ == '__main__':
    unittest.main()

