from typing import Union

from src.infra.database.connection import Connection
from src.domain.entity.coupon import Coupon
from src.domain.repository.coupon_repository import CouponRepository


class CouponRepositoryPostgreSQL(CouponRepository):

    def __init__(self, connection: Connection):
        self.__connection = connection

    def get_by_code(self, code: str) -> Union[Coupon, None]:
        coupon_data = self.__connection.query('select * from coupon where code = %s', [code])
        if len(coupon_data) == 0:
            return None
        coupon_data = coupon_data[0]
        coupon = Coupon(code=coupon_data[0], percentage=float(coupon_data[1]), expired_date=coupon_data[2])
        return coupon

    def calculate_discount(self, amount: float, coupon: Coupon) -> float:
        discount = coupon.calculate_discount(amount)
        return discount
