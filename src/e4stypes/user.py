from typing import Dict
"""
Contains a User class.
"""


class User:
    """
    Represents a user of the website.
    """

    def __init__(self, display_name: str, email: str, password: str):
        # Private instance attributes
        self._display_name = display_name
        self._email = email
        self._password = password

        # Public instance attributes
        self.address = ""
        self.venmo_user = ""
        self.allows_shipping = False
        self.allows_pickup = True

    def to_dict(self) -> Dict:
        return {
            "display name" : self.get_display_name(), 
            "email" : self.get_email(),
            "password" : self.get_password()
        }

    def get_display_name(self) -> str:
        return self._display_name

    def get_email(self) -> str:
        return self._email

    def get_password(self) -> str:
        return self._password

    def edit_settings(self) -> type(None):
        pass

    def logout(self) -> type(None):
        pass

    def login(self, email: str, password: str) -> type(None):
        pass

    @classmethod
    def register(cls):
        pass

    def post_item(self, item_id: str) -> type(None):
        """Implements Seller.post_item()"""
        pass

    def edit_item(self, item_id: str) -> type(None):
        """Implements Seller.edit_item()"""
        pass

    def send_message_to_seller(self, seller: str) -> bool:
        """Implements Customer.send_message_to_seller()"""
        pass

    def purchase_item(self, item_id: str) -> type(None):
        """Implements Customer.purchase_item()"""
        pass
