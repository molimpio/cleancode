class Dimension:

    def __init__(self, width: float, height: float, length: float):
        self.__width = width
        self.__height = height
        self.__length = length

    def get_volume(self) -> float:
        return (self.__width / 100) * (self.__height / 100) * (self.__length / 100)
