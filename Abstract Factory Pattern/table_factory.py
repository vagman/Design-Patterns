from small_table import SmallTable
from medium_table import MediumTable
from big_table import BigTable

class TableFactory:

    @staticmethod
    def get_table(table_type: str):
        try:
            if (table_type == "BigTable"):
                return BigTable()
            if (table_type == "MediumTable"):
                return MediumTable()
            if (table_type == "SmallTable"):
                return SmallTable()
            raise AssertionError("Table type given not found.")
        except AssertionError as e:
            print(e)
        return None