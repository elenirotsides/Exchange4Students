from decimal import Decimal


class Item:
    """
    An item listed by a user on the site.
    """
    def __init__(self, title: str, desc: str, price: Decimal, weight: float,
                 seller: str):
        # Private instance attributes
        self._item_id: str = ""
        self._title: str = title
        self._description: str = desc
        self._price: Decimal = price
        self._weight: float = weight
        self._seller: str = seller
        self._condition: str = ""
        #self._img: str = ""

        # Public instance attributes
        self.quantity: int = 1

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

    # def get_img(self) -> str:
    #      return self._img

    # def update_img(self, img_name: str):
    #     self._img = "/uploads" + img_name

