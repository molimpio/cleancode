from typing import Union, List
from datetime import datetime

from src.domain.entity.coupon import Coupon
from src.domain.repository.coupon_repository import CouponRepository


class CouponRepositoryMemory(CouponRepository):

    def __init__(self):
        self.__coupons: List[Coupon] = [
            Coupon('VALE20', 20, datetime(2022, 10, 10)),
            Coupon('VALE50', 20, datetime(2021, 10, 10))
        ]

    def get_by_code(self, code: str) -> Union[Coupon, None]:
        coupon = [coupon for coupon in self.__coupons if coupon.code == code]
        if coupon:
            return coupon[0]
        return None

    def calculate_discount(self, amount: float, coupon: Coupon) -> float:
        return coupon.calculate_discount(amount)
