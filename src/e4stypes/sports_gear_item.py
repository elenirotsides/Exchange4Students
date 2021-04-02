from decimal import Decimal
from typing import List

from item import Item
from clothing_item import ClothingGender, ClothingSize


class SportsGearItem(Item):
    def __init__(self, item_id: str, title: str, desc: str, price: Decimal,
                 weight: float, seller: str, gear_type: str,
                 size: ClothingSize, gender: ClothingGender):
        super().__init__(item_id, title, desc, price, weight, seller)

        # Private instance attributes
        self._gear_type: str = gear_type
        self._size: str = size
        self._gender: ClothingGender = gender

    def get_gear_type(self) -> str:
        return self._gear_type

    def get_size(self) -> ClothingSize:
        return self._size

    def get_gender(self) -> List[int]:
        return self._gender
