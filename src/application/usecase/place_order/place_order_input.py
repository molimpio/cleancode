from datetime import datetime


class PlaceOrderInput:

    def __init__(self, cpf: str, order_itens, coupon: str = None, date: datetime = datetime.now()):
        self.__cpf = cpf
        self.__order_itens = order_itens
        self.__coupon = coupon
        self.__date = date

    @property
    def cpf(self):
        return self.__cpf

    @property
    def order_itens(self):
        return self.__order_itens

    @property
    def coupon(self):
        return self.__coupon

    @property
    def date(self):
        return self.__date
