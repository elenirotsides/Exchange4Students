from decimal import Decimal
from enum import Enum

from item import Item

class ClothingGender(Enum):
    UNISEX = 0
    FEMALE = 1
    MALE = 2

class ClothingSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    EXTRA_LARGE = 3

class ClothingItem(Item):

    def __init__(self, item_id: int,
                 title: str,
                 desc: str,
                 price: Decimal,
                 weight: float,
                 seller: str,
                 garment_type: str,
                 size: CLOTHING_SIZE,
                 gender: CLOTHING_GENDER,
                 color: str):
        super().__init__(item_id, title, desc, price, weight, seller)

