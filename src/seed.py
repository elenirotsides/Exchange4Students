from pathlib import Path
from pymongo import MongoClient
from e4stypes.database import Database
from e4stypes.book_item import BookItem
from e4stypes.clothing_item import ClothingItem, ClothingGender, ClothingSize
from e4stypes.electronic_item import ElectronicItem
from e4stypes.furniture_item import FurnitureItem
from e4stypes.sports_gear_item import SportsGearItem
from e4stypes.user import User
"""
This is a file you can run to seed your database!
Purpose: every time the database gets edited/refactored, the exchange4students db needs to be
         deleted, and new fake data needs to be inserted for testing so the new schema is being
         reflected....that's an unnecessarily lengthy process. It wastes time and draws the
         focus away from what's important.
How to use: There is no neeed to manually delete and insert items. Simply run this file to do
            all the work for you. When the db schema gets edited, you can simply make any
            corresponding edits here as well to reflect that, and then the file can be run
            again. Running the file will delete the db for you, and will create a new one with
            data in a matter of seconds.

Let me know if there are any questions,
~Eleni :)
"""


def drop_db():
    """Drops the database"""
    client = MongoClient("mongodb://localhost:27017/")
    client.drop_database("exchange4students")
    print("Database successfully dropped")
    print("----------------------------------------------")


def add_clothing():
    """Adds 5 clothing documents to the clothing collection"""
    print("Attempting to seed the clothing collection.....")
    print()

    shirt_path = Path("shirt.png")

    shirt = ClothingItem(
        "Lightly worn Hollister shirt",
        "Really cute, lightweight, and comfortable shirt! In good condition and selling \
            for less than the original price.",
        15.00,
        0.16,
        "Sarah",
        "shirt",
        ClothingSize.MEDIUM,
        ClothingGender.FEMALE,
        "olive green",
    )
    shirt.set_image_filepath(shirt_path)
    Database.add_item(shirt)
    print("Shirt has been successfully added")

    jeans = ClothingItem(
        "A pair of cute Levi's",
        "Classic wash jeans, well taken care of. They just don't fit me anymore hahah!",
        30.00,
        0.20,
        "Eleni",
        "jeans",
        ClothingSize.LARGE,
        ClothingGender.FEMALE,
        "classic blue wash",
    )
    jeans.set_image_filepath(shirt_path)
    Database.add_item(jeans)
    print("Jeans have been successfully added")

    blazer = ClothingItem(
        "A professional blazer",
        "Its interview season! You probably need something to wear, so why not this cute \
            blazer? Don't worry, its in great condition!",
        20.50,
        0.10,
        "Grace",
        "blazer",
        ClothingSize.SMALL,
        ClothingGender.UNISEX,
        "black",
    )
    blazer.set_image_filepath(shirt_path)
    Database.add_item(blazer)
    print("Blazer has been successfully added")

    sweater = ClothingItem(
        "Fluffy sweater",
        "So snuggly and warm, my grandma knitted it",
        13.00,
        0.13,
        "Julio",
        "sweater",
        ClothingSize.MEDIUM,
        ClothingGender.UNISEX,
        "Orange",
    )
    sweater.set_image_filepath(shirt_path)
    Database.add_item(sweater)
    print("Sweater has been successfully added")

    jacket = ClothingItem(
        "Leather jacket, vintage",
        "Really cool vintage leather jacket. A bit worn but that's the point",
        150.00,
        3.00,
        "David",
        "leather jacket",
        ClothingSize.LARGE,
        ClothingGender.MALE,
        "black",
    )
    jacket.set_image_filepath(shirt_path)
    Database.add_item(jacket)
    print("Leather jacket has been successfully added")

    print()
    print("Done seeding the clothing collection!")
    print("----------------------------------------------")


def add_books():
    """Adds 5 book documents to the book collection"""
    print("Attempting to seed the book collection.....")
    print()

    book_path = Path("book.png")

    book1 = BookItem(
        "Harry Potter pack for sale",
        "All 7 books! Come and get 'em!",
        50.00,
        8,
        "Sarah",
        "Harry Potter - The Collection",
        3,
        "-",
    )
    book1.set_image_filepath(book_path)
    Database.add_item(book1)
    print("book1 has been successfully added")

    book2 = BookItem(
        "Econ textbook, never used",
        "Idk why I bought this to begin with. Never used it.",
        75.00,
        4,
        "Grace",
        "Introduction to Engineering Economics",
        7,
        "ECON-235",
    )
    book2.set_image_filepath(book_path)
    Database.add_item(book2)
    print("book2 has been successfully added")

    book3 = BookItem(
        "Comp Sci book for Prof Lowe's class",
        "Good condition, you're gonna need this for his class...",
        35.00,
        5.6,
        "Eleni",
        "Data Structures in Java",
        12,
        "CS-550",
    )
    book3.set_image_filepath(book_path)
    Database.add_item(book3)
    print("book3 has been successfully added")

    book4 = BookItem(
        "Chemistry textbook, freshman I'm looking at you!",
        "For freshman year chem, selling for much cheaper than other students.",
        30.00,
        6,
        "Julio",
        "Introduction to Chemistry, a Hollistic Aproach",
        2,
        "CH-115",
    )
    book4.set_image_filepath(book_path)
    Database.add_item(book4)
    print("book4 has been successfully added")

    book5 = BookItem(
        "Calculus textbook",
        "A little worn out, but still usable.",
        28.00,
        16,
        "David",
        "Calculus made Simple, a Student Friendly Guide",
        3,
        "MA-111",
    )
    book5.set_image_filepath(book_path)
    Database.add_item(book5)
    print("book5 has been successfully added")

    print()
    print("Done seeding the book collection!")
    print("----------------------------------------------")


def add_electronics():
    """Adds 5 electronic documents to the electronic collection"""
    print("Attempting to seed the electronic collection.....")
    print()

    electronic_path = Path("electronic.png")

    ps1 = ElectronicItem(
        "Archaic PS1, come get herrrrr",
        "Classic, worth a lot of moolah, don't miss out!",
        10000.00,
        10,
        "Sarah",
        "PlayStation",
        "First one ever",
        [10, 20, 10],
    )
    ps1.set_image_filepath(electronic_path)
    Database.add_item(ps1)
    print("ps1 has been successfully added")

    ps2 = ElectronicItem(
        "Calling all vintage video game console collectors! Selling PS2!!!",
        "An oldie but a goodie.",
        50.00,
        10,
        "Grace",
        "PlayStation",
        "2nd",
        [10, 20, 10],
    )
    ps2.set_image_filepath(electronic_path)
    Database.add_item(ps2)
    print("ps2 have been successfully added")

    ps3 = ElectronicItem(
        "PS3",
        "Still works like a charm!",
        100.00,
        10,
        "Eleni",
        "PlayStation",
        "3rd",
        [10, 20, 10],
    )
    ps3.set_image_filepath(electronic_path)
    Database.add_item(ps3)
    print("ps3 has been successfully added")

    ps4 = ElectronicItem(
        "PS4",
        "Selling for cheaper than you can get it at the stores!",
        200.00,
        10,
        "Julio",
        "PlayStation",
        "4th",
        [10, 20, 10],
    )
    ps4.set_image_filepath(electronic_path)
    Database.add_item(ps4)
    print("ps4 has been successfully added")

    ps5 = ElectronicItem(
        "PS5! YES YOU READ THAT CORRECTLY!",
        "You know what this is bois",
        100000.00,
        10,
        "David",
        "PlayStation",
        "5th",
        [10, 20, 10],
    )
    ps5.set_image_filepath(electronic_path)
    Database.add_item(ps5)
    print("ps5 has been successfully added")

    print()
    print("Done seeding the electronic collection!")
    print("----------------------------------------------")


def add_sports_gear():
    """Adds 5 sports gear documents to the sports collection"""
    print("Attempting to seed the sports collection.....")
    print()

    football_path = Path("football.png")

    skiis = SportsGearItem(
        "Used skiis",
        "In great condition, also a great price!",
        40.00,
        1.05,
        "Sarah",
        "Skiis",
        ClothingSize.MEDIUM,
        ClothingGender.UNISEX,
    )
    skiis.set_image_filepath(football_path)
    Database.add_item(skiis)
    print("skiis have been successfully added")

    helmet = SportsGearItem(
        "Bicycle helmet",
        "I have a small head, like a child.",
        15.00,
        0.20,
        "Eleni",
        "Helmet",
        ClothingSize.SMALL,
        ClothingGender.UNISEX,
    )
    helmet.set_image_filepath(football_path)
    Database.add_item(helmet)
    print("helmet has been successfully added")

    snowboard = SportsGearItem(
        "Snowboard, no longer need it",
        "My mom bought me a new one for my birthday, so I no longer need this. Great condition.",
        50.00,
        0.10,
        "Grace",
        "Snowboard",
        ClothingSize.SMALL,
        ClothingGender.UNISEX,
    )
    snowboard.set_image_filepath(football_path)
    Database.add_item(snowboard)
    print("snowboard has been successfully added")

    tennis_racket = SportsGearItem(
        "Tennis Racket, signed by Serena Williams",
        "Its signed!!!",
        1500.00,
        0.67,
        "Julio",
        "Tennis Racket",
        ClothingSize.MEDIUM,
        ClothingGender.UNISEX,
    )
    tennis_racket.set_image_filepath(football_path)
    Database.add_item(tennis_racket)
    print("tennis racket has been successfully added")

    roller_skates = SportsGearItem(
        "Roller skates, great condition",
        "Super cute and sparkly!",
        45.00,
        2.00,
        "David",
        "Roller Skates",
        ClothingSize.LARGE,
        ClothingGender.UNISEX,
    )
    roller_skates.set_image_filepath(football_path)
    Database.add_item(roller_skates)
    print("roller skates have been successfully added")

    print()
    print("Done seeding the sports collection!")
    print("----------------------------------------------")


def add_furniture():
    """Adds 5 furniture documents to the furniture collection"""
    print("Attempting to seed the furniture collection.....")
    print()

    chair_path = Path("chair.png")

    couch = FurnitureItem(
        "Comfy couch",
        "Well loved, but still in pretty good condition",
        60.00,
        40,
        "Sarah",
        "Couch",
        "beige",
        [50, 20, 10],
    )
    couch.set_image_filepath(chair_path)
    Database.add_item(couch)
    print("couch has been successfully added")

    table = FurnitureItem(
        "Dining room table",
        "Wooden dining room table. Has a few scuffs, but not bad!",
        30.00,
        15,
        "Grace",
        "Table",
        "wood",
        [40, 20, 40],
    )
    table.set_image_filepath(chair_path)
    Database.add_item(table)
    print("table has been successfully added")

    bed = FurnitureItem(
        "Bed Frame",
        "Just selling the bed frame, you'll have \
        to get your own mattress",
        55.00,
        50,
        "Eleni",
        "Bed",
        "white",
        [10, 20, 10],
    )
    bed.set_image_filepath(chair_path)
    Database.add_item(bed)
    print("bed has been successfully added")

    desk = FurnitureItem(
        "Ikea desk, no longer need it",
        "In great condition, this is truly a steal",
        60.00,
        35,
        "Julio",
        "Ikea Desk",
        "navy",
        [20, 20, 30],
    )
    desk.set_image_filepath(chair_path)
    Database.add_item(desk)
    print("desk has been successfully added")

    shelf = FurnitureItem(
        "Book shelf, never used",
        "Brand new",
        110.00,
        25,
        "David",
        "Book Shelf",
        "black",
        [10, 20, 100],
    )
    shelf.set_image_filepath(chair_path)
    Database.add_item(shelf)
    print("shelf has been successfully added")

    print()
    print("Done seeding the furniture collection!")
    print("----------------------------------------------")

def add_user():
    ''' Adds 1 user to the database.'''
    print("Attempting to add user to database...")
    print()

    user1 = User("Grace Miguel", "gracem730@gmail.com", "12345")
    Database.add_user(user1)
    print("User 1 has been successfully added.")



# Calling the functions
drop_db()
add_clothing()
add_books()
add_electronics()
add_sports_gear()
add_furniture()
add_user()
print("DATABASE SEEDING COMPLETE")
