from ifurniture_factory import IFurnitureFactory
from table_factory import TableFactory
from chair_factory import ChairFactory

class FurnitureFactory(IFurnitureFactory):

    def get_furniture(furniture_type: str):

        # This could possibly be a database instead of a list
        available_chairs = ["BigChair", "MediumChair", "SmallChair"]
        available_tables = ["BigTable", "MediumTable", "SmallTable"]

        try:
            if furniture_type in available_chairs:
                return ChairFactory.get_chair(furniture_type)
            if furniture_type in available_tables:
                return TableFactory.get_table(furniture_type)
            raise AssertionError("Cannot find the furniture type you specified.")
        except AssertionError as e:
            print(e)
        return None
