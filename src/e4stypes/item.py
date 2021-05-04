from decimal import Decimal
from pathlib import Path


class Item:
    """
    An item listed by a user on the site.
    """

    def __init__(
        self, title: str, desc: str, price: Decimal, weight: float, seller: str
    ):
        # Private instance attributes
        self._item_id: str = ""
        self._title: str = title
        self._description: str = desc
        self._price: Decimal = price
        self._weight: float = weight
        self._seller: str = seller
        self._condition: str = ""
        self._image = Path()
        self.is_sold = False

    def get_item_id(self) -> str:
        return self._item_id

    def set_item_id(self, item_id: str) -> type(None):
        self._item_id = item_id

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

    def get_image_filepath(self) -> type(None):
        return self._image

    def set_image_filepath(self, filepath: Path) -> type(None):
        self._image = filepath

    def price_string(self) -> str:
        return str(self.get_price().quantize(Decimal("1.00")))
