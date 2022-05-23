import unittest
from datetime import datetime

from src.domain.entity.coupon import Coupon


class CouponTestCase(unittest.TestCase):
    def test_deve_criar_coupon_desconto(self):
        coupon = Coupon('VALE20', 20)
        is_expired = coupon.is_expired()
        self.assertFalse(is_expired)

    def test_deve_criar_coupon_desconto_expirado(self):
        coupon = Coupon('VALE20', 20, datetime(2022, 1, 1))
        is_expired = coupon.is_expired(datetime(2022, 2, 1))
        self.assertTrue(is_expired)

    def test_deve_criar_coupon_desconto_calcular_desconto(self):
        coupon = Coupon('VALE20', 20)
        discount = coupon.calculate_discount(1000)
        self.assertEqual(200, discount)


if __name__ == '__main__':
    unittest.main()
