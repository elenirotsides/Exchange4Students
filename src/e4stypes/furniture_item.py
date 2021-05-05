from decimal import Decimal
from typing import List, Dict

from .item import Item


class FurnitureItem(Item):
    def __init__(
        self,
        title: str,
        desc: str,
        price: Decimal,
        weight: float,
        seller: str,
        furnishing_type: str,
        color: str,
        dimensions: List[int],
    ):
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

    def to_dict(self) -> Dict:
        return {
            "title": self.get_title(),
            "desc": self.get_description(),
            "price": float(self.get_price()),
            "weight": self.get_weight(),
            "seller": self.get_seller(),
            "furnishing_type": self.get_furnishing_type(),
            "color": self.get_color(),
            "dimensions": self.get_dimensions(),
            "img": str(self.get_image_filepath()),
            "is_sold": self.is_sold,
        }
