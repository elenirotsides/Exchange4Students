from decimal import Decimal
from typing import List

from item import Item
import pymongo

# establish connection with database
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# create the databse if it doesn't already exist
db = myclient.exchange4students

# create book collection
electronic_col = db.electronic

class ElectronicItem(Item):
    def __init__(self, item_id: str, title: str, desc: str, price: Decimal,
                 weight: float, seller: str, electronic_type: str, model: str,
                 dimensions: List[int]):
        super().__init__(item_id, title, desc, price, weight, seller)

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
