from abc import ABCMeta, abstractmethod, ABC

"""
    - Let's say you have an object that has 2 required attr and 5 optional ones

"""
class IHouseBuilder(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        "Build type"

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        "Build material"

    @staticmethod
    @abstractmethod
    def set_number_doors(number):
        "Number of doors"

    @staticmethod
    @abstractmethod
    def set_number_windows(number):
        "Number of windows"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"


class House:
    def __init__(self, building_type="Apartment", doors=0, windows=0, wall_material='Brick'):
        self.wall_material = wall_material
        # Apartment, Bungalow, Caravan, Castle, Duplex, HouseBoat, Igloo
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def construction(self):
        return f"This is a {self.wall_material}" \
               f"{self.building_type} with {self.doors}" \
               f"doors and {self.windows} window(s)"


class HouseBuilder(IHouseBuilder):
    """The concrete class that implement a house builder"""

    def __init__(self):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def set_number_doors(self, number):
        self.house.doors = number
        return self

    def set_number_windows(self, number):
        self.house.windows = number
        return self

    def get_result(self):
        return self.house.construction()


class HouseBoatDirector:

    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_wall_material("Wood") \
            .set_building_type("House Boat") \
            .set_number_doors(6) \
            .set_number_windows(8) \
            .get_result()


class CastleDirector:

    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_wall_material("Sandstone") \
            .set_building_type("Castle") \
            .set_number_doors(100) \
            .set_number_windows(200) \
            .get_result()


c1 = CastleDirector().construct()
print(c1)
