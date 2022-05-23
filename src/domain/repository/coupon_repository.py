from abc import ABC, abstractmethod
from typing import Union

from src.domain.entity.coupon import Coupon


class CouponRepository(ABC):
    @abstractmethod
    def get_by_code(self, code: str) -> Union[Coupon, None]:
        pass

    @abstractmethod
    def calculate_discount(self, amount: float, coupon: Coupon) -> float:
        pass
