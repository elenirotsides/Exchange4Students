from abc import ABCMeta

"""
Inteface for methods that a User acting as a Customer would use.

This interface expects these methods to be implemented:

def send_message_to_seller(seller_username: str) -> bool:
def purchase_item(item_id: int) -> None:

"""
class Customer(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'send_message_to_seller') and
                callable(subclass.send_message_to_seller) and
                hasattr(subclass, 'purchase_item') and
                callable(subclass.purchase_item))


