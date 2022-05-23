class OrderItem:

    def __init__(self, id_item: int, price: float, quantity: float):
        self.__id_item = id_item
        self.__price = price
        self.__quantity = quantity

    @property
    def id_item(self):
        return self.__id_item

    @property
    def quantity(self):
        return self.__quantity

    def get_total(self) -> float:
        return self.__price * self.__quantity
