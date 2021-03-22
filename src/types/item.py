from decimal import Decimal
from typing import List

class Item:
    """
    An item listed by a user on the site.
    """

    def __init__(self, item_id: int, title: str, desc: str, price: Decimal, weight: float, seller: str):
        # Private instance attributes
        self._item_id: int     = item_id
        self._title: str       = title
        self._description: str = desc
        self._price: Decimal   = price
        self._weight: float    = weight
        self._seller: str      = seller
        self._condition: str   = ""

        # Public instance attributes
        self.quantity: int = 1

    def get_item_id(self) -> int:
        return self._item_id

    def get_title(self) -> str:
        return self._title

    def get_description(self) -> str:
        return self._description

    def get_price(self) -> Decimal:
        return self._price

    def get_weight(self) -> float:
        return self._weight

    def get_seller(self) -> str:
        return self._seller

    def get_condition(self) -> str:
        return self._condition

    @classmethod
    def get_all(cls) -> List[Item]:
        pass

    @classmethod
    def get_item_by_id(cls, item_id: int) -> Item:
        pass

    @classmethod
    def get_item_by_catergory(cls, category: str) -> List[Item]:
        pass

