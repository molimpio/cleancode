from datetime import datetime


class Coupon:

    def __init__(self, code: str, percentage: int, expired_date: datetime = None):
        self.__code = code
        self.__percentage = percentage
        self.__expired_date = expired_date

    @property
    def code(self):
        return self.__code

    def is_expired(self, today: datetime = datetime.now()) -> bool:
        if self.__expired_date is None:
            return False
        return self.__expired_date < today

    def calculate_discount(self, amount: float) -> float:
        return (amount * self.__percentage) / 100
