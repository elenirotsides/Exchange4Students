from typing import List
from decimal import Decimal
from item import Item
from bson import ObjectId
import pymongo
from book_item import BookItem
from clothing_item import ClothingItem, ClothingGender, ClothingSize
from electronic_item import ElectronicItem
from furniture_item import FurnitureItem
from sports_gear_item import SportsGearItem

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


class Database:
    @classmethod
    def get_all(cls) -> List[Item]:
        return (Database.get_item_by_category("Clothing") +
                Database.get_item_by_category("Book") +
                Database.get_item_by_category("Furniture") +
                Database.get_item_by_category("Electronic") +
                Database.get_item_by_category("Sports Gear"))

    @classmethod
    def get_item_by_id(cls, item_id: str) -> Item:
        # Stores the result of the search
        get_clothing = clothing_col.find_one({'_id': ObjectId(item_id)})
        get_book = book_col.find_one({'_id': ObjectId(item_id)})
        get_furniture = furniture_col.find_one({'_id': ObjectId(item_id)})
        get_electronic = electronic_col.find_one({'_id': ObjectId(item_id)})
        get_sports = sports_gear_col.find_one({'_id': ObjectId(item_id)})

        # Returns the Item if a item was found with the given item_id
        if get_clothing:
            item = ClothingItem(get_clothing["title"], get_clothing["desc"],
                                Decimal(get_clothing["price"]),
                                get_clothing["weight"], get_clothing["seller"],
                                get_clothing["garment_type"],
                                ClothingSize(get_clothing["size"]),
                                ClothingGender(get_clothing["gender"]),
                                get_clothing["color"])
            item.set_item_id(get_clothing["_id"])
            return item
        if get_book:
            item = BookItem(get_book["title"], get_book["desc"],
                            Decimal(get_book["price"]), get_book["weight"],
                            get_book["seller"], get_book["book_title"],
                            get_book["edition"], get_book["course_number"])
            item.set_item_id(get_book["_id"])
            return item
        if get_furniture:
            item = FurnitureItem(get_furniture["title"], get_furniture["desc"],
                                 Decimal(get_furniture["price"]),
                                 get_furniture["weight"],
                                 get_furniture["seller"],
                                 get_furniture["furnishing_type"],
                                 get_furniture["color"],
                                 get_furniture["dimensions"])
            item.set_item_id(get_furniture["_id"])
            return item
        if get_electronic:
            item = ElectronicItem(
                get_electronic["title"], get_electronic["desc"],
                Decimal(get_electronic["price"]), get_electronic["weight"],
                get_electronic["seller"], get_electronic["electronic_type"],
                get_electronic["model"], get_electronic["dimensions"])
            item.set_item_id(get_electronic["_id"])
            return item
        if get_sports:
            item = SportsGearItem(get_sports["title"], get_sports["desc"],
                                  Decimal(get_sports["price"]),
                                  get_sports["weight"], get_sports["seller"],
                                  get_sports["gear_type"],
                                  ClothingSize(get_sports["size"]),
                                  ClothingGender(get_sports["gender"]))
            item.set_item_id(get_sports["_id"])
            return item
        raise RuntimeError(
            "get_item_by_id: could not find item with passed id")

    @classmethod
    def get_item_by_category(cls, category: str) -> List[Item]:
        # Gets items by category
        # Note: currently not accounting for empty collections.
        # we can add checks for empty collections later if this causes problems.
        items = []
        if category == 'Clothing':
            item_dicts = clothing_col.find({})
            for item_dict in item_dicts:
                # instantiate a ClothingItem based on the
                # fields of the item dict and then append
                # it to the running array
                item = ClothingItem(item_dict["title"], item_dict["desc"],
                                    Decimal(item_dict["price"]),
                                    item_dict["weight"], item_dict["seller"],
                                    item_dict["garment_type"],
                                    ClothingSize(item_dict["size"]),
                                    ClothingGender(item_dict["gender"]),
                                    item_dict["color"])
                item.set_item_id(item_dict["_id"])
                items.append(item)
            return items
        elif category == 'Book':
            item_dicts = book_col.find({})
            for item_dict in item_dicts:
                item = BookItem(item_dict["title"], item_dict["desc"],
                                Decimal(item_dict["price"]),
                                item_dict["weight"], item_dict["seller"],
                                item_dict["book_title"], item_dict["edition"],
                                item_dict["course_number"])
                item.set_item_id(item_dict["_id"])
                items.append(item)
        elif category == 'Furniture':
            item_dicts = furniture_col.find({})
            for item_dict in item_dicts:
                item = FurnitureItem(item_dict["title"], item_dict["desc"],
                                     Decimal(item_dict["price"]),
                                     item_dict["weight"], item_dict["seller"],
                                     item_dict["furnishing_type"],
                                     item_dict["color"],
                                     item_dict["dimensions"])
                item.set_item_id(item_dict["_id"])
                items.append(item)
        elif category == 'Electronic':
            item_dicts = electronic_col.find({})
            for item_dict in item_dicts:
                item = ElectronicItem(item_dict["title"], item_dict["desc"],
                                      Decimal(item_dict["price"]),
                                      item_dict["weight"], item_dict["seller"],
                                      item_dict["electronic_type"],
                                      item_dict["model"],
                                      item_dict["dimensions"])
                item.set_item_id(item_dict["_id"])
                items.append(item)
        elif category == 'Sports Gear':
            item_dicts = sports_gear_col.find({})
            for item_dict in item_dicts:
                item = SportsGearItem(item_dict["title"], item_dict["desc"],
                                      Decimal(item_dict["price"]),
                                      item_dict["weight"], item_dict["seller"],
                                      item_dict["gear_type"],
                                      ClothingSize(item_dict["size"]),
                                      ClothingGender(item_dict["gender"]))
                item.set_item_id(item_dict["_id"])
                items.append(item)
        else:
            raise RuntimeError("get_item_by_category: category undefined")
        return items
