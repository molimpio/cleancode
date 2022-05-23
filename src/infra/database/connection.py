from abc import ABC, abstractmethod
from typing import Union


class Connection(ABC):

    @abstractmethod
    def query(self, sql: str, params: list) -> Union[list, None]:
        pass

    @abstractmethod
    def insert(self, sql: str, params: list) -> int:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
