from decimal import Decimal

"""
An item listed by a user on the site.
"""
class Item:

    def __init__(self, item_id: int, title: str, desc: str, price: Decimal, weight: float, seller: str):
        # Private instance attributes
        self._item_id = item_id
        self._title = title
        self._description = desc
        self._price = price
        self._weight = weight
        self._seller = seller
        self._condition = ""

        # Public instance attributes
        self.quantity = 1

    def get_item_id(self): -> int:
        return self._item_id

    def get_title(self): -> str:
        return self._title

    def get_description(self): -> str:
        return self._description

    def get_price(self): -> Decimal:
        return self._price

    def get_weight(self): -> float:
        return self._weight

    def get_seller(self): -> str:
        return self._seller

    def get_condition(self): -> str:
        return self._condition

    @classmethod
    def get_all() -> list[Item]:
        pass

    @clasmethod
    def get_item_by_id(cls, item_id: int) -> Item:
        pass

    @classmethod
    def get_item_by_catergory(cls, category: str) -> list[Item]:
        pass

