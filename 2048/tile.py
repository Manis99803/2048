class Tile:
    def __init__(self, x, y, value = "_"):
        self.__x = x
        self.__y = y
        self.__value = "_"

    @property
    def x_coordinate(self):
        return self.__x

    @property
    def y_coordinate(self):
        return self.__y

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
