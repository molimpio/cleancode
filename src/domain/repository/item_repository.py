from abc import ABC, abstractmethod
from typing import Union

from src.domain.entity.item import Item


class ItemRepository(ABC):
    @abstractmethod
    def get_by_id(self, id_item: int) -> Union[Item, None]:
        pass
