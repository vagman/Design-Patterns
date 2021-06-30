from big_chair import BigChair
from medium_chair import MediumChair
from small_chair import SmallChair

class ChairFactory:

    @staticmethod
    def get_chair(chair_type: str):
        try:
            if (chair_type == "BigChair"):
                return BigChair()
            if (chair_type == "MediumChair"):
                return MediumChair()
            if (chair_type == "SmallChair"):
                return SmallChair()
            raise AssertionError("Chair type given not found.")
        except AssertionError as e:
            print(e)
        return None