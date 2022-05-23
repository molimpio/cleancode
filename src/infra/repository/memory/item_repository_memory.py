from typing import Union, List

from src.domain.entity.item import Item
from src.domain.entity.dimension import Dimension
from src.domain.repository.item_repository import ItemRepository


class ItemRepositoryMemory(ItemRepository):

    def __init__(self):
        self.__items: List[Item] = [
            Item(1, 'Instrumentos musicais', 'Guitarra', 1000, Dimension(100, 30, 10), 3),
            Item(2, 'Instrumentos musicais', 'Amplificador', 5000, Dimension(100, 50, 50), 20),
            Item(3, 'Instrumentos musicais', 'Cabo', 30, Dimension(10, 10, 10), 1)
        ]

    def get_by_id(self, id_item: int) -> Union[Item, None]:
        item = [item for item in self.__items if item.id_item == id_item]
        if item:
            return item[0]
        return None
