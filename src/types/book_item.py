from decimal import Decimal

from item import Item

class BookItem(Item):

    def __init__(self, item_id: int,
                 title: str,
                 desc: str,
                 price: Decimal,
                 weight: float,
                 seller: str,
                 book_title: str,
                 edition: int,
                 course_number: int):
        super().__init__(item_id, title, desc, price, weight, seller)

        # Private instance attributes
        self._book_title: str    = book_title
        self._edition: int       = edition
        self._course_number: int = course_number

    def get_book_title(self) -> str:
        return self._book_title

    def get_edition(self) -> int:
        return self._edition

    def get_course_number(self) -> int:
        return self._course_number