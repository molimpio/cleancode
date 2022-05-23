from datetime import datetime


class OrderCode:

    def __init__(self, date: datetime, sequence: int):
        self.__value = self._generate_code(date, sequence)

    @staticmethod
    def _generate_code(date: datetime, sequence: int) -> str:
        year = date.year
        return str(year) + str(sequence).rjust(8, "0")

    @property
    def value(self):
        return self.__value
