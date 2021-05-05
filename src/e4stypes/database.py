from typing import List
from decimal import Decimal
from enum import Enum
from bson import ObjectId
import pymongo
from .item import Item
from .book_item import BookItem
from .clothing_item import ClothingItem, ClothingGender, ClothingSize
from .electronic_item import ElectronicItem
from .furniture_item import FurnitureItem
from .sports_gear_item import SportsGearItem

# establish connection with database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# create the databse if it doesn't already exist
db = myclient.exchange4students

# create collections
clothing_col = db.clothing
book_col = db.book
furniture_col = db.furniture
electronic_col = db.electronic
sports_gear_col = db.sports_gear


class Category(Enum):
    CLOTHING = "Clothing"
    BOOK = "Book"
    FURNITURE = "Furniture"
    ELECTRONIC = "Electronic"
    SPORTS_GEAR = "Sports Gear"


# Helper methods


def _first_found_item(clo_query, book_query, furn_query, elec_query, spo_query) -> Item:
    # Returns the Item if a item was found with the given item_id
    if clo_query:
        item = ClothingItem(
            clo_query["title"],
            clo_query["desc"],
            Decimal(clo_query["price"]),
            clo_query["weight"],
            clo_query["seller"],
            clo_query["garment_type"],
            ClothingSize(clo_query["size"]),
            ClothingGender(clo_query["gender"]),
            clo_query["color"],
        )
        item.set_item_id(clo_query["_id"])
        item.set_image_filepath(clo_query["img"])
        return item
    if book_query:
        item = BookItem(
            book_query["title"],
            book_query["desc"],
            Decimal(book_query["price"]),
            book_query["weight"],
            book_query["seller"],
            book_query["book_title"],
            book_query["edition"],
            book_query["course_number"],
        )
        item.set_item_id(book_query["_id"])
        item.set_image_filepath(book_query["img"])
        return item
    if furn_query:
        item = FurnitureItem(
            furn_query["title"],
            furn_query["desc"],
            Decimal(furn_query["price"]),
            furn_query["weight"],
            furn_query["seller"],
            furn_query["furnishing_type"],
            furn_query["color"],
            furn_query["dimensions"],
        )
        item.set_item_id(furn_query["_id"])
        item.set_image_filepath(furn_query["img"])
        return item
    if elec_query:
        item = ElectronicItem(
            elec_query["title"],
            elec_query["desc"],
            Decimal(elec_query["price"]),
            elec_query["weight"],
            elec_query["seller"],
            elec_query["electronic_type"],
            elec_query["model"],
            elec_query["dimensions"],
        )
        item.set_item_id(elec_query["_id"])
        item.set_image_filepath(elec_query["img"])
        return item
    if spo_query:
        item = SportsGearItem(
            spo_query["title"],
            spo_query["desc"],
            Decimal(spo_query["price"]),
            spo_query["weight"],
            spo_query["seller"],
            spo_query["gear_type"],
            ClothingSize(spo_query["size"]),
            ClothingGender(spo_query["gender"]),
        )
        item.set_item_id(spo_query["_id"])
        item.set_image_filepath(spo_query["img"])
        return item
    raise RuntimeError("get_item_by_id: could not find item with passed id")


def _all_items_from_item_dicts(item_dicts, category):
    items = []
    if category == Category.CLOTHING:
        for item_dict in item_dicts:
            # instantiate a ClothingItem based on the
            # fields of the item dict and then append
            # it to the running array
            item = ClothingItem(
                item_dict["title"],
                item_dict["desc"],
                Decimal(item_dict["price"]),
                item_dict["weight"],
                item_dict["seller"],
                item_dict["garment_type"],
                ClothingSize(item_dict["size"]),
                ClothingGender(item_dict["gender"]),
                item_dict["color"],
            )
            item.set_item_id(item_dict["_id"])
            item.set_image_filepath(item_dict["img"])
            items.append(item)
        return items
    if category == Category.BOOK:
        for item_dict in item_dicts:
            item = BookItem(
                item_dict["title"],
                item_dict["desc"],
                Decimal(item_dict["price"]),
                item_dict["weight"],
                item_dict["seller"],
                item_dict["book_title"],
                item_dict["edition"],
                item_dict["course_number"],
            )
            item.set_item_id(item_dict["_id"])
            item.set_image_filepath(item_dict["img"])
            items.append(item)
        return items
    if category == Category.FURNITURE:
        item_dicts = furniture_col.find({})
        for item_dict in item_dicts:
            item = FurnitureItem(
                item_dict["title"],
                item_dict["desc"],
                Decimal(item_dict["price"]),
                item_dict["weight"],
                item_dict["seller"],
                item_dict["furnishing_type"],
                item_dict["color"],
                item_dict["dimensions"],
            )
            item.set_item_id(item_dict["_id"])
            item.set_image_filepath(item_dict["img"])
            items.append(item)
        return items
    if category == Category.ELECTRONIC:
        for item_dict in item_dicts:
            item = ElectronicItem(
                item_dict["title"],
                item_dict["desc"],
                Decimal(item_dict["price"]),
                item_dict["weight"],
                item_dict["seller"],
                item_dict["electronic_type"],
                item_dict["model"],
                item_dict["dimensions"],
            )
            item.set_item_id(item_dict["_id"])
            item.set_image_filepath(item_dict["img"])
            items.append(item)
        return items
    if category == Category.SPORTS_GEAR:
        for item_dict in item_dicts:
            item = SportsGearItem(
                item_dict["title"],
                item_dict["desc"],
                Decimal(item_dict["price"]),
                item_dict["weight"],
                item_dict["seller"],
                item_dict["gear_type"],
                ClothingSize(item_dict["size"]),
                ClothingGender(item_dict["gender"]),
            )
            item.set_item_id(item_dict["_id"])
            item.set_image_filepath(item_dict["img"])
            items.append(item)
        return items
    raise RuntimeError("get_item_by_category: category undefined")


class Database:
    @classmethod
    def get_all(cls) -> List[Item]:
        return (
            Database.get_item_by_category(Category.CLOTHING)
            + Database.get_item_by_category(Category.BOOK)
            + Database.get_item_by_category(Category.FURNITURE)
            + Database.get_item_by_category(Category.ELECTRONIC)
            + Database.get_item_by_category(Category.SPORTS_GEAR)
        )

    @classmethod
    def get_item_by_id(cls, item_id: str) -> Item:
        # Stores the result of the search
        get_clothing = clothing_col.find_one({"_id": ObjectId(item_id)})
        get_book = book_col.find_one({"_id": ObjectId(item_id)})
        get_furniture = furniture_col.find_one({"_id": ObjectId(item_id)})
        get_electronic = electronic_col.find_one({"_id": ObjectId(item_id)})
        get_sports = sports_gear_col.find_one({"_id": ObjectId(item_id)})

        return _first_found_item(
            get_clothing, get_book, get_furniture, get_electronic, get_sports
        )

    @classmethod
    def get_item_by_category(cls, category: Category) -> List[Item]:
        # Gets items by category
        # Note: currently not accounting for empty collections.
        # we can add checks for empty collections later if this causes problems.
        item_dicts = None
        if category == Category.CLOTHING:
            item_dicts = clothing_col.find({})
        elif category == Category.BOOK:
            item_dicts = book_col.find({})
        elif category == Category.FURNITURE:
            item_dicts = furniture_col.find({})
        elif category == Category.ELECTRONIC:
            item_dicts = electronic_col.find({})
        elif category == Category.SPORTS_GEAR:
            item_dicts = sports_gear_col.find({})
        else:
            raise RuntimeError("get_item_by_category: category undefined")

        return _all_items_from_item_dicts(item_dicts, category)

    @classmethod
    def add_book(cls, book: BookItem) -> type(None):
        # making insertion
        book_col.insert_one(book.to_dict())

    @classmethod
    def add_clothing(cls, clothing: ClothingItem) -> type(None):
        # making insertion
        clothing_col.insert_one(clothing.to_dict())

    @classmethod
    def add_electronic(cls, electronic: ElectronicItem) -> type(None):
        # making insertion
        electronic_col.insert_one(electronic.to_dict())

    @classmethod
    def add_furniture(cls, furniture: FurnitureItem) -> type(None):
        # making insertion
        furniture_col.insert_one(furniture.to_dict())

    @classmethod
    def add_sports_gear(cls, sports_gear: SportsGearItem) -> type(None):
        # making insertion
        sports_gear_col.insert_one(sports_gear.to_dict())

    @classmethod
    def add_item(cls, item: Item) -> type(None):
        if isinstance(item, ClothingItem):
            Database.add_clothing(item)
        elif isinstance(item, BookItem):
            Database.add_book(item)
        elif isinstance(item, FurnitureItem):
            Database.add_furniture(item)
        elif isinstance(item, ElectronicItem):
            Database.add_electronic(item)
        elif isinstance(item, SportsGearItem):
            Database.add_sports_gear(item)
        else:
            raise RuntimeError("add_item: unknown item subclass")

    @classmethod
    def search_item(cls, search_term) -> List[Item]:
        search_term.strip()
        result = []
        database_content = Database.get_all()
        current_item = {}
        term_list = []

        for word in database_content:
            current_item = word
            title_string = current_item.get_title().lower()
            term_list = title_string.split()
            if search_term.lower() in term_list:
                result.append(current_item)
        return result

    @classmethod
    def update_sold(cls, item) -> type(None):
        if isinstance(item, ClothingItem):
            clothing_col.update_one(
                {"_id": item.get_item_id()}, {"$set": {"is_sold": True}}
            )
        elif isinstance(item, BookItem):
            book_col.update_one(
                {"_id": item.get_item_id()}, {"$set": {"is_sold": True}}
            )
        elif isinstance(item, FurnitureItem):
            furniture_col.update_one(
                {"_id": item.get_item_id()}, {"$set": {"is_sold": True}}
            )
        elif isinstance(item, ElectronicItem):
            electronic_col.update_one(
                {"_id": item.get_item_id()}, {"$set": {"is_sold": True}}
            )
        elif isinstance(item, SportsGearItem):
            sports_gear_col.update_one(
                {"_id": item.get_item_id()}, {"$set": {"is_sold": True}}
            )
        else:
            raise RuntimeError("Could not update item")
