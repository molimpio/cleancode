from src.domain.repository.coupon_repository import CouponRepository


class ValidateCoupon:

    def __init__(self, coupon_repository: CouponRepository):
        self.__coupon_repository = coupon_repository

    def execute(self, code: str) -> bool:
        coupon = self.__coupon_repository.get_by_code(code)

        if coupon is None:
            return False

        return coupon.is_expired()
