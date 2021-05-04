from decimal import Decimal
from typing import Dict
from .item import Item


class BookItem(Item):
    def __init__(
        self,
        title: str,
        desc: str,
        price: Decimal,
        weight: float,
        seller: str,
        book_title: str,
        edition: int,
        course_number: int,
    ):
        super().__init__(title, desc, price, weight, seller)

        # Private instance attributes
        self._book_title: str = book_title
        self._edition: int = edition
        self._course_number: str = course_number

    def get_book_title(self) -> str:
        return self._book_title

    def get_edition(self) -> int:
        return self._edition

    def get_course_number(self) -> str:
        return self._course_number

    def to_dict(self) -> Dict:
        return {
            "title": self.get_title(),
            "desc": self.get_description(),
            "price": float(self.get_price()),
            "weight": self.get_weight(),
            "seller": self.get_seller(),
            # 'img': self.get_img(),
            "book_title": self.get_book_title(),
            "edition": self.get_edition(),
            "course_number": self.get_course_number(),
            "img": str(self.get_image_filepath()),
            "is_sold": self.is_sold
        }
