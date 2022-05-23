
class PlaceOrderOutput:

    def __init__(self, total: float, code: str):
        self.__total = total
        self.__code = code

    @property
    def total(self):
        return self.__total

    @property
    def code(self):
        return self.__code
