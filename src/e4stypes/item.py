from decimal import Decimal
from typing import List
from bson import ObjectId
import pymongo

# establish connection with database
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# create the databse if it doesn't already exist
db = myclient.exchange4students

# create collections
clothing_col = db.clothing
book_col = db.book
furniture_col = db.furniture
electronic_col = db.electronic
sports_gear_col = db.sports_gear


class Item:
    """
    An item listed by a user on the site.
    """
    def __init__(self, item_id: str, title: str, desc: str, price: Decimal,
                 weight: float, seller: str):
        # Private instance attributes
        self._item_id: str = item_id
        self._title: str = title
        self._description: str = desc
        self._price: Decimal = price
        self._weight: float = weight
        self._seller: str = seller
        self._condition: str = ""

        # Public instance attributes
        self.quantity: int = 1

    def get_item_id(self) -> str:
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
        # find all items in item collection, returns list of dictionaries
        all_items = list(clothing_col.find({})) + list(
            book_col.find({})) + list(furniture_col.find({})) + list(
                electronic_col.find({})) + list(sports_gear_col.find({}))
        return all_items

    @classmethod
    def get_item_by_id(cls, item_id: str) -> Item:
        # Stores the result of the search
        get_clothing = clothing_col.find_one({'_id': ObjectId(item_id)})
        get_book = book_col.find_one({'_id': ObjectId(item_id)})
        get_furniture = furniture_col.find_one({'_id': ObjectId(item_id)})
        get_electronic = electronic_col.find_one({'_id': ObjectId(item_id)})
        get_sports = sports_gear_col.find_one({'_id': ObjectId(item_id)})

        # Returns the item dict if a item was found with the given item_id
        if get_clothing:
            return dict(get_clothing)
        if get_book:
            return dict(get_book)
        if get_furniture:
            return dict(get_furniture)
        if get_electronic:
            return dict(get_electronic)
        if get_sports:
            return dict(get_sports)

    @classmethod
    def get_item_by_category(cls, category: str) -> List[Item]:
        # Gets items by category
        # Note: currently not accounting for empty collections. I can add checks for empty collections later if this causes problems.
        if category == 'Clothing':
            items = clothing_col.find({})
            return list(items)
        if category == 'Book':
            items = book_col.find({})
            return list(items)
        if category == 'Furniture':
            items = furniture_col.find({})
            return list(items)
        if category == 'Electronic':
            items = electronic_col.find({})
            return list(items)
        if category == 'Sports Gear':
            items = sports_gear_col.find({})
            return list(items)
