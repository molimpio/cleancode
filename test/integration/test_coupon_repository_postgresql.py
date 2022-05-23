import unittest
from src.infra.database.postgre_sql_connection_adapter import PostgreSQLConnectionAdapter
from src.infra.repository.postgresql.coupon_repository_postgresql import CouponRepositoryPostgreSQL


class CouponRepositoryPostgreSSQLTestCase(unittest.TestCase):
    def test_deve_retornar_coupon_pelo_codigo(self):
        connection = PostgreSQLConnectionAdapter()
        coupon_repository = CouponRepositoryPostgreSQL(connection)
        coupon = coupon_repository.get_by_code('VALE20')
        self.assertEqual(coupon.code, 'VALE20')
        connection.close()

    def test_deve_calcular_percentual_desconto_pelo_coupon(self):
        connection = PostgreSQLConnectionAdapter()
        coupon_repository = CouponRepositoryPostgreSQL(connection)
        coupon = coupon_repository.get_by_code('VALE20')
        discount = coupon_repository.calculate_discount(1000.0, coupon)
        self.assertEqual(discount, 200.0)
        connection.close()


if __name__ == '__main__':
    unittest.main()
