from decimal import Decimal
from typing import List
from .database import Database
from .item import Item


class OrderInformation:
    def __init__(self, item_list: List[Item], total_amount: Decimal):
        self.item_list: List[Item] = item_list
        self.total_amount: Decimal = total_amount

    def add_to_cart(self, item_id: str) -> type(None):
        self.item_list.append(item_id)
        return self.item_list

    def remove_from_cart(self, item_id: str) -> type(None):
        self.item_list.remove(item_id)
        return self.item_list

    def calculate_total_amount(self) -> Decimal:
        self.total_amount = 0
        for item in self.item_list:
            specific_item = Database.get_item_by_id(item)
            price = specific_item.get_price()
            self.total_amount += price
        return self.total_amount

    def confirm(self) -> bool:
        pass

    def select_exchange_type(self) -> type(None):
        pass
