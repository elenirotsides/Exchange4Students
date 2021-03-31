from decimal import Decimal
from typing import List

from item import Item


class OrderInformation:
    def __init__(self, item_list: List[Item], total_amount: Decimal):
        self.item_list: List[Item] = item_list
        self.total_amount: Decimal = total_amount

    def add_to_cart(self, item_id: str) -> type(None):
        pass

    def remove_from_cart(self, item_id: str) -> type(None):
        pass

    def calculate_total_amount(self) -> Decimal:
        pass

    def confirm(self) -> bool:
        pass

    def select_exchange_type(self) -> type(None):
        pass
