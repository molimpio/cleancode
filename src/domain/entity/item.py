from src.domain.entity.dimension import Dimension


class Item:

    def __init__(self, id_item: int, category: str, description: str, price: float, dimension: Dimension = None,
                 weight: float = None):
        self.__id_item = id_item
        self.__category = category
        self.__description = description
        self.__price = price
        self.__dimension = dimension
        self.__weight = weight

    @property
    def description(self) -> str:
        return self.__description

    @property
    def id_item(self):
        return self.__id_item

    @property
    def price(self):
        return self.__price

    def get_volume(self) -> float:
        if self.__dimension:
            return self.__dimension.get_volume()
        return 0.0

    def get_density(self) -> float:
        if self.__weight and self.__dimension:
            return self.__weight / self.__dimension.get_volume()
        else:
            return 0.0
