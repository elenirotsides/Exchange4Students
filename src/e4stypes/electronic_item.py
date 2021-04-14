from decimal import Decimal
from typing import List, Dict
from .item import Item


class ElectronicItem(Item):
    def __init__(
        self,
        title: str,
        desc: str,
        price: Decimal,
        weight: float,
        seller: str,
        electronic_type: str,
        model: str,
        dimensions: List[int],
    ):
        super().__init__(title, desc, price, weight, seller)

        # Private instance attributes
        self._electronic_type: str = electronic_type
        self._model: str = model
        self._dimensions: List[int] = dimensions

    def get_electronic_type(self) -> str:
        return self._electronic_type

    def get_model(self) -> str:
        return self._model

    def get_dimensions(self) -> List[int]:
        return self._dimensions

    def to_dict(self) -> Dict:
        return {
            "title": self.get_title(),
            "desc": self.get_description(),
            "price": float(self.get_price()),
            "weight": self.get_weight(),
            "seller": self.get_seller(),
            "electronic_type": self.get_electronic_type(),
            "model": self.get_model(),
            "dimensions": self.get_dimensions(),
            "img": str(self.get_image_filepath()),
        }
