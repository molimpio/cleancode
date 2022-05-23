from typing import List, Union

from src.domain.entity.order import Order
from src.domain.repository.order_repository import OrderRepository


class OrderRepositoryMemory(OrderRepository):

    def get_by_code(self, code: str) -> Union[Order, None]:
        pass

    def __init__(self):
        self.__orders: List[Order] = []

    def save(self, order: Order) -> int:
        self.__orders.append(order)
        return len(self.__orders) - 1

    def count(self) -> int:
        return len(self.__orders)
