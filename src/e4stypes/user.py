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

    def get_display_name(self) -> str:
        return self._display_name

    def get_email(self) -> str:
        return self._email

    def get_password(self) -> str:
        return self._password
