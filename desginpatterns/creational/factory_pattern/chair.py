from abc import ABCMeta, abstractmethod


class ChairFactory:

    @staticmethod
    def get_chair(chair_type: str) -> object:
        if chair_type == "Small Chair":
            return SmallChair(40, 60, 50)


class IChair(metaclass=ABCMeta):

    @abstractmethod
    def get_dimension(self) -> dict:
        pass


class SmallChair(IChair):
    def __init__(self, height, width, depth):
        self._height = height
        self._width = width
        self._depth = depth

    def get_dimension(self) -> dict:
        return {
            "width": self._width,
            "height": self._height,
            "depth": self._depth
        }


# Client

small_chair = ChairFactory.get_chair('Small Chair')
print(small_chair.get_dimension())