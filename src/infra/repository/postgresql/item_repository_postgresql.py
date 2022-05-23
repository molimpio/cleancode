from typing import Union

from src.infra.database.connection import Connection
from src.domain.entity.item import Item
from src.domain.entity.dimension import Dimension
from src.domain.repository.item_repository import ItemRepository


class ItemRepositoryPostgreSQL(ItemRepository):

    def __init__(self, connection: Connection):
        self.__connection = connection

    def get_by_id(self, id_item: int) -> Union[Item, None]:
        item_data = self.__connection.query('select * from item where id_item = %s', [id_item])
        if len(item_data) == 0:
            return None
        item_data = item_data[0]
        item = Item(id_item=item_data[0], category=item_data[1], description=item_data[2], price=float(item_data[3]),
                    dimension=Dimension(width=item_data[4], height=item_data[5], length=item_data[6]),
                    weight=item_data[7])
        return item
