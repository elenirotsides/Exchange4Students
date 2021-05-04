import os
from pathlib import Path
from decimal import Decimal
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from flask_fontawesome import FontAwesome
from e4stypes.database import Category, Database
from e4stypes.book_item import BookItem
from e4stypes.clothing_item import ClothingItem
from e4stypes.electronic_item import ElectronicItem
from e4stypes.furniture_item import FurnitureItem
from e4stypes.sports_gear_item import SportsGearItem
from e4stypes.order_information import OrderInformation

basedir = Path(os.path.dirname(os.path.realpath(__file__)))
uploadsdir = basedir.joinpath("static")
cart = OrderInformation([], 0)
order_info_keys = ["first", "last", "email", "venmo", "address", "country",
"state", "zip", "place", "date", "time"]
order_info_dict = dict.fromkeys(order_info_keys, None)
final_cart_list = []
final_total = 0

app = Flask(__name__)
fa = FontAwesome(app)

app.config["SECRET_KEY"] = "Howdy D6"
if not uploadsdir.exists():
    uploadsdir.mkdir()
app.config["UPLOADED_PHOTOS_DEST"] = str(uploadsdir)


@app.route("/", methods=["GET", "POST"])
def get_home():
    if request.method == "POST":
        if "add_to_cart" in request.form:
            item_id = request.form["add_to_cart"]
            cart.add_to_cart(item_id)
        if "remove_from_cart" in request.form:
            item_id = request.form["remove_from_cart"]
            cart.remove_from_cart(item_id)
    return render_template(
        "/home.html",
        items=Database.get_all(),
        cart=cart,
        listing_title="All Items",
    )


@app.route("/books", methods=["GET", "POST"])
def get_books():
    if request.method == "POST":
        if "add_to_cart" in request.form:
            item_id = request.form["add_to_cart"]
            cart.add_to_cart(item_id)
        if "remove_from_cart" in request.form:
            item_id = request.form["remove_from_cart"]
            cart.remove_from_cart(item_id)
    return render_template(
        "/listing.html",
        items=Database.get_item_by_category(Category.BOOK),
        listing_title="Books",
        cart=cart,
    )


@app.route("/clothes", methods=["GET", "POST"])
def get_clothes():
    if request.method == "POST":
        if "add_to_cart" in request.form:
            item_id = request.form["add_to_cart"]
            cart.add_to_cart(item_id)
        if "remove_from_cart" in request.form:
            item_id = request.form["remove_from_cart"]
            cart.remove_from_cart(item_id)
    return render_template(
        "/listing.html",
        items=Database.get_item_by_category(Category.CLOTHING),
        listing_title="Clothes",
        cart=cart,
    )


@app.route("/electronics", methods=["GET", "POST"])
def get_electronics():
    if request.method == "POST":
        if "add_to_cart" in request.form:
            item_id = request.form["add_to_cart"]
            cart.add_to_cart(item_id)
        if "remove_from_cart" in request.form:
            item_id = request.form["remove_from_cart"]
            cart.remove_from_cart(item_id)
    return render_template(
        "/listing.html",
        items=Database.get_item_by_category(Category.ELECTRONIC),
        listing_title="Electronics",
        cart=cart,
    )


@app.route("/sports", methods=["GET", "POST"])
def get_sports():
    if request.method == "POST":
        if "add_to_cart" in request.form:
            item_id = request.form["add_to_cart"]
            cart.add_to_cart(item_id)
        if "remove_from_cart" in request.form:
            item_id = request.form["remove_from_cart"]
            cart.remove_from_cart(item_id)
    return render_template(
        "/listing.html",
        items=Database.get_item_by_category(Category.SPORTS_GEAR),
        listing_title="Sports",
        cart=cart,
    )


@app.route("/furniture", methods=["GET", "POST"])
def get_furniture():
    if request.method == "POST":
        if "add_to_cart" in request.form:
            item_id = request.form["add_to_cart"]
            cart.add_to_cart(item_id)
        if "remove_from_cart" in request.form:
            item_id = request.form["remove_from_cart"]
            cart.remove_from_cart(item_id)
    return render_template(
        "/listing.html",
        items=Database.get_item_by_category(Category.FURNITURE),
        listing_title="Furniture",
        cart=cart,
    )


@app.route("/sell", methods=["GET", "POST"])
def get_sell():
    if request.method == "POST":
        # grab form data in order they appear in sell.html
        category = request.form["category_drop_val"]
        post_title = request.form["post_title_val"]
        price = request.form["price_val"]
        title = request.form["title_val"]
        edition = request.form["ed_val"]
        if request.form["length_val"] != "":
            dimensions = [
                int(request.form["length_val"]),
                int(request.form["width_val"]),
                int(request.form["height_val"]),
            ]
        weight = request.form["weight_val"]
        color = request.form["color_val"]
        # type is a key word
        type_val = request.form["type_val"]
        course_num = request.form["course_num_val"]
        size = request.form["size_val"]
        gender = request.form["gender_val"]
        model = request.form["model_val"]
        description = request.form["comments_val"]
        seller = request.form["seller_val"]

        # photo upload
        image_file = request.files["file"]
        filename = secure_filename(image_file.filename)
        image_filepath = uploadsdir.joinpath(filename)
        image_file.save(str(image_filepath))

        # error handling
        if Decimal(price.strip()) < 0:
            price = "0"
        if title == "":
            title = "Title was not provided"
        if edition == "":
            edition = "Edition was not provided"
        if weight == "":
            weight = "0"
        if course_num == "":
            course_num = "Course Number was not provided"
        if color == "":
            color = "Color was not provided"
        if type_val == "":
            type_val = "Type was not provided"
        if request.form["length_val"] == "":
            dimensions = [
                0,
                0,
                0,
            ]
        if model == "":
            model = "Model was not provided"

        # create item and add item to database
        if category == "books":
            item = BookItem(
                post_title,
                description,
                Decimal(price.strip()),
                float(weight.strip()),
                seller,
                title,
                edition,
                course_num,
            )
            item.set_image_filepath(filename)
            Database.add_item(item)
        elif category == "furniture":
            item = FurnitureItem(
                post_title,
                description,
                Decimal(price.strip()),
                float(weight.strip()),
                seller,
                type_val,
                color,
                dimensions,
            )
            item.set_image_filepath(filename)
            Database.add_item(item)
        elif category == "clothes":
            item = ClothingItem(
                post_title,
                description,
                Decimal(price.strip()),
                float(weight.strip()),
                seller,
                type_val,
                int(size),
                int(gender),
                color,
            )
            item.set_image_filepath(filename)
            Database.add_item(item)
        elif category == "sports":
            item = SportsGearItem(
                post_title,
                description,
                Decimal(price.strip()),
                float(weight.strip()),
                seller,
                type_val,
                int(size),
                int(gender),
            )
            item.set_image_filepath(filename)
            Database.add_item(item)
        elif category == "electronics":
            item = ElectronicItem(
                post_title,
                description,
                Decimal(price.strip()),
                float(weight.strip()),
                seller,
                type_val,
                model,
                dimensions,
            )
            item.set_image_filepath(filename)
            Database.add_item(item)
        return redirect("/item_posted")
    return render_template("/sell.html", cart=cart)


@app.route("/view/<item_id>", methods=["GET", "POST"])
def get_view(item_id):
    item = Database.get_item_by_id(item_id)
    if isinstance(item, ClothingItem):
        if request.method == "POST":
            if "add_to_cart" in request.form:
                item_id = request.form["add_to_cart"]
                cart.add_to_cart(item_id)
            if "remove_from_cart" in request.form:
                item_id = request.form["remove_from_cart"]
                cart.remove_from_cart(item_id)
        return render_template(
            "/view_clothing.html",
            item=item,
            small=item.get_size() == 0,
            medium=item.get_size() == 1,
            large=item.get_size() == 2,
            xlarge=item.get_size() == 3,
            unisex=item.get_gender() == 0,
            female=item.get_gender() == 1,
            male=item.get_gender() == 2,
            cart=cart,
        )

    if isinstance(item, BookItem):
        if request.method == "POST":
            if "add_to_cart" in request.form:
                item_id = request.form["add_to_cart"]
                cart.add_to_cart(item_id)
            if "remove_from_cart" in request.form:
                item_id = request.form["remove_from_cart"]
                cart.remove_from_cart(item_id)
        return render_template("/view_book.html", item=item, cart=cart)

    if isinstance(item, FurnitureItem):
        if request.method == "POST":
            if "add_to_cart" in request.form:
                item_id = request.form["add_to_cart"]
                cart.add_to_cart(item_id)
            if "remove_from_cart" in request.form:
                item_id = request.form["remove_from_cart"]
                cart.remove_from_cart(item_id)
        return render_template("/view_furniture.html", item=item, cart=cart)

    if isinstance(item, ElectronicItem):
        if request.method == "POST":
            if "add_to_cart" in request.form:
                item_id = request.form["add_to_cart"]
                cart.add_to_cart(item_id)
            if "remove_from_cart" in request.form:
                item_id = request.form["remove_from_cart"]
                cart.remove_from_cart(item_id)
        return render_template("/view_electronic.html", item=item, cart=cart)

    if isinstance(item, SportsGearItem):
        if request.method == "POST":
            if "add_to_cart" in request.form:
                item_id = request.form["add_to_cart"]
                cart.add_to_cart(item_id)
            if "remove_from_cart" in request.form:
                item_id = request.form["remove_from_cart"]
                cart.remove_from_cart(item_id)
        return render_template(
            "/view_sports_gear.html",
            item=item,
            small=item.get_size() == 0,
            medium=item.get_size() == 1,
            large=item.get_size() == 2,
            xlarge=item.get_size() == 3,
            unisex=item.get_gender() == 0,
            female=item.get_gender() == 1,
            male=item.get_gender() == 2,
            cart=cart,
        )


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template("/404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    # will only be triggered when debug mode is off, this is default flask behaivior
    print(error)
    return render_template("/500.html"), 500

@app.route("/search", methods=["GET", "POST"])
def get_search():
    if request.method == "POST":
        if"search_term" in request.form:
            term = request.form["search_term"]
            return render_template(
                "/listing.html",
                items=Database.search_item(term),
                listing_title="Search Results", cart=cart
            )
        if"add_to_cart" in request.form:
            item_id = request.form["add_to_cart"]
            cart.add_to_cart(item_id)
        if"remove_from_cart" in request.form:
            item_id = request.form["remove_from_cart"]
            cart.remove_from_cart(item_id)
    return render_template(
        "/listing.html",
        listing_title="Search Results", cart=cart
    )


@app.route("/item_posted", methods=["GET", "POST"])
def get_item_posted():
    return render_template("/item_posted.html", cart=cart)


@app.route("/checkout", methods=["GET", "POST"])
def get_checkout():
    total = 0
    for item in cart.item_list:
        total += item.get_price()
    if request.method == "POST":
        if "drop_val" in request.form:
            category = request.form["drop_val"]
            order_info_dict["first"] = request.form["firstName_val"]  
            order_info_dict["last"] = request.form["lastName_val"]
            order_info_dict["email"] = request.form["email_val"]
            order_info_dict["venmo"] = request.form["v-name"]
            if category == "Ship":
                order_info_dict["address"] = request.form["address_val"]
                order_info_dict["country"] = request.form["country_val"]
                order_info_dict["state"] = request.form["state_val"]
                order_info_dict["zip"] = request.form["zip_val"]
            if category == "Dropoff/Pickup":
                order_info_dict["place"] = request.form["place_val"]
                order_info_dict["date"] = request.form["date_val"]
                order_info_dict["time"] = request.form["time_val"]
        print(cart.item_list)
        cart.confirm()
        cart.reset_cart()
        final_cart_list = cart.item_list
        final_total = total
        #email stuff here

    return render_template("/checkout.html", cart=cart, total=total)


if __name__ == "__main__":
    app.run(debug=True)
