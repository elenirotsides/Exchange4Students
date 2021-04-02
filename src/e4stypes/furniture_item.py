from decimal import Decimal
from typing import List

from item import Item

import pymongo

# establish connection with database
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# create the databse if it doesn't already exist
db = myclient.exchange4students

# create furniture collection if it doesn't already exist
furniture_col = db.furniture


class FurnitureItem(Item):
    def __init__(self, item_id: str, title: str, desc: str, price: Decimal,
                 weight: float, seller: str, furnishing_type: str, color: str,
                 dimensions: List[int]):
        super().__init__(item_id, title, desc, price, weight, seller)

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
