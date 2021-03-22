from decimal import Decimal

from item import Item

class Book(Item):

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
        self._book_title = book_title
        self._edition = edition
        self._course_number = course_number

    def get_book_title(self): -> str:
        return self._book_title

    def get_edition(self) -> int:
        return self._edition

    def get_course_number(self) -> int:
        return self._course_number
