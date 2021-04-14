from abc import ABCMeta


class Seller(metaclass=ABCMeta):
    """
    Inteface for methods that a User acting as a Seller would use.

    This interface expects these methods to be implemented:

    def post_item(item_id: int) -> None:
    def edit_item(item_id: int) -> None:

    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "post_item")
            and callable(subclass.post_item)
            and hasattr(subclass, "edit_item")
            and callable(subclass.edit_item)
        )
