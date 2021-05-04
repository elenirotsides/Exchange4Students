from decimal import Decimal
from typing import List
from .database import Database
from .item import Item
from bson import ObjectId


class OrderInformation:
    def __init__(self, item_list: List[Item], total_amount: Decimal):
        self.item_list: List[Item] = item_list
        self.total_amount: Decimal = total_amount
        self.buyer = None

    def add_to_cart(self, item_id: str) -> type(None):
        item_to_add = Database.get_item_by_id(item_id)
        item_list_ids = []
        for item in self.item_list:
            item_list_ids.append(item.get_item_id())
        if ObjectId(item_id) not in item_list_ids:
            self.item_list.append(item_to_add)

    def remove_from_cart(self, item_id: str) -> type(None):
        for item_list_item in self.item_list:
            if ObjectId(item_id) == item_list_item.get_item_id():
                self.item_list.remove(item_list_item)

    def calculate_total_amount(self) -> Decimal:
        self.total_amount = 0
        for item in self.item_list:
            specific_item = Database.get_item_by_id(item)
            price = specific_item.get_price()
            self.total_amount += price
        return self.total_amount

    def confirm(self) -> type(None):
        for item in self.item_list:
            Database.update_sold(item)
            print(item.is_sold)

    def reset_cart(self) -> type(None):
        self.item_list = []
        self.total_amount = 0
        self.buyer = None
