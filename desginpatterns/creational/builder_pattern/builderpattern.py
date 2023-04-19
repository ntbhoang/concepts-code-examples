from abc import abstractmethod, ABCMeta


class IBuilder(metaclass=ABCMeta):
    """The Builder Interface"""
    
    @staticmethod
    @abstractmethod
    def build_part_a():
        ...

    @staticmethod
    @abstractmethod
    def build_part_b():
        ...

    @staticmethod
    @abstractmethod
    def build_part_c():
        ...

    @staticmethod
    @abstractmethod
    def get_result():
        ...


class Product:
    def __init__(self):
        self.parts = []


class Builder(IBuilder):
    """The implementation class of IBuilder"""
    
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return self.product


class Director:
    "The Director, building a complex representation"

    @staticmethod
    def construct():
        return Builder().build_part_a() \
                        .build_part_b() \
                        .build_part_c() \
                        .get_result()


PRODUCT = Director.construct()
print(PRODUCT.parts)