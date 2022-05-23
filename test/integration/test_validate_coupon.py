import unittest

from src.infra.repository.memory.coupon_repository_memory import CouponRepositoryMemory
from src.application.usecase.coupon.validate_coupon import ValidateCoupon


class ValidateCouponTest(unittest.TestCase):
    def test_deve_validar_coupon_desconto_valido(self):
        coupon_repository = CouponRepositoryMemory()
        validate_coupon = ValidateCoupon(coupon_repository)
        is_expired = validate_coupon.execute('VALE20')
        self.assertFalse(is_expired)

    def test_deve_nao_validar_coupon_desconto_por_que_nao_existe(self):
        coupon_repository = CouponRepositoryMemory()
        validate_coupon = ValidateCoupon(coupon_repository)
        invalid = validate_coupon.execute('VALE100')
        self.assertFalse(invalid)
        

if __name__ == '__main__':
    unittest.main()
