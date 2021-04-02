from decimal import Decimal
from typing import List

from item import Item


class FurnitureItem(Item):
    def __init__(self, title: str, desc: str, price: Decimal, weight: float,
                 seller: str, furnishing_type: str, color: str,
                 dimensions: List[int]):
        super().__init__(title, desc, price, weight, seller)

        # Private instance attributes
        self._furnishing_type: str = furnishing_type
        self._color: str = color
        self._dimensions: List[int] = dimensions

    def get_furnishing_type(self) -> str:
        return self._furnishing_type

    def get_color(self) -> str:
        return self._color

    def get_dimensions(self) -> List[int]:
        return self._dimensions
