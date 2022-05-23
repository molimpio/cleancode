import unittest
from src.infra.database.postgre_sql_connection_adapter import PostgreSQLConnectionAdapter
from src.infra.repository.postgresql.order_repository_postgresql import OrderRepositoryPostgreSQL
from src.domain.entity.order import Order


class OrderRepositoryPostgreSQLTest(unittest.TestCase):
    def test_repositorio_salvar_order(self):
        connection = PostgreSQLConnectionAdapter()
        order_repository = OrderRepositoryPostgreSQL(connection)
        order = Order('935.411.347-80')
        order_bd = order_repository.save(order)
        self.assertEqual(order_bd.cpf.value, '935.411.347-80')
        connection.close()

    def test_repositorio_buscar_order_pelo_codigo(self):
        connection = PostgreSQLConnectionAdapter()
        order_repository = OrderRepositoryPostgreSQL(connection)
        order = order_repository.get_by_code('202200000001')
        self.assertEqual(order.code.value, '202200000001')
        connection.close()

    def test_repositorio_contar_qtde_orders(self):
        connection = PostgreSQLConnectionAdapter()
        order_repository = OrderRepositoryPostgreSQL(connection)
        orders = order_repository.count()
        self.assertTrue(orders > 0)
        connection.close()


if __name__ == '__main__':
    unittest.main()
