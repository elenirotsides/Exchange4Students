
import pymongo
#from database import Database
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient.exchange4students 
from clothing_item import ClothingItem, ClothingSize, ClothingGender

clothing_col = db.clothing

tshirt = ClothingItem("", "red", "ugly shirt", 12.0, 12, "Grace Miguel", "t-shirt", ClothingSize.SMALL, ClothingGender.FEMALE, "red" )
clothing = {
        'title': tshirt.get_title(),
        'description': tshirt.get_description(),
        'price': tshirt.get_price(),
        'weight': tshirt.get_weight(),
        'seller': tshirt.get_seller(),
        'garment_type': tshirt.get_garment_type(),
        'size': tshirt.get_size(),
        'gender':tshirt.get_gender(),
        'color': tshirt.get_color()
    }
clothing_col.insert_one(clothing)