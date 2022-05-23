
class SimulateFreightInput:

    def __init__(self, order_itens):
        self.__order_itens = order_itens

    @property
    def order_itens(self):
        return self.__order_itens
