from abc import ABC, abstractmethod
from typing import Union
from src.domain.entity.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> Union[Order, None]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def get_by_code(self, code: str) -> Union[Order, None]:
        pass
