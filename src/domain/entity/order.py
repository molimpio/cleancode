from typing import List
from datetime import datetime
from src.domain.entity.cpf import Cpf
from src.domain.entity.order_item import OrderItem
from src.domain.entity.freight import Freight
from src.domain.entity.coupon import Coupon
from src.domain.entity.item import Item
from src.domain.entity.order_code import OrderCode


class Order:

    def __init__(self, cpf: str, issue_date: datetime = datetime.now(), sequence: int = 1):
        self.__cpf = Cpf(cpf)
        self.__order_itens: List[OrderItem] = []
        self.__freight = Freight()
        self.__issue_date = issue_date
        self.__coupon: Coupon = None
        self.__sequence = sequence
        self.__code = OrderCode(issue_date, sequence)

    @property
    def sequence(self) -> int:
        return self.__sequence

    @property
    def issue_date(self):
        return self.__issue_date

    @property
    def freight(self) -> Freight:
        return self.__freight

    @property
    def cpf(self) -> Cpf:
        return self.__cpf

    @property
    def coupon(self) -> str:
        if self.__coupon:
            return self.__coupon.code
        else:
            return ''

    @property
    def freight(self):
        return self.__freight

    @property
    def code(self):
        return self.__code

    def add_item(self, item: Item, quantity: float) -> None:
        self.__freight.add_item(item, quantity)
        self.__order_itens.append(OrderItem(item.id_item, item.price, quantity))

    def add_coupon(self, coupon: Coupon) -> None:
        if coupon.is_expired(self.__issue_date) is False:
            self.__coupon = coupon

    def get_total(self) -> float:
        total = 0

        for order_item in self.__order_itens:
            total += order_item.get_total()

        if self.__coupon:
            total -= self.__coupon.calculate_discount(total)

        freight = self.__freight.get_total()
        total += freight
        return total
