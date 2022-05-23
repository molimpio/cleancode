from src.domain.entity.item import Item


class Freight:
    __distance = 1000

    def __init__(self):
        self.__total = 0.0

    def add_item(self, item: Item, quantity: float) -> None:
        self.__total += (item.get_volume() * self.__distance * (item.get_density() / 100)) * quantity

    def get_total(self) -> float:
        if 0 < self.__total < 10:
            return 10.0
        return self.__total
