import os
#from pyrebase import auth
from pathlib import Path
from decimal import Decimal
from flask import Flask, render_template, request, session, abort, redirect
import google
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol, requests
from google.oauth2 import id_token
import google.auth.transport.requests
from werkzeug.utils import secure_filename
from e4stypes.database import Category, Database
from e4stypes.book_item import BookItem
from e4stypes.clothing_item import ClothingItem
from e4stypes.electronic_item import ElectronicItem
from e4stypes.furniture_item import FurnitureItem
from e4stypes.sports_gear_item import SportsGearItem
import pathlib








basedir = Path(os.path.dirname(os.path.realpath(__file__)))
uploadsdir = basedir.joinpath("static")

app = Flask(__name__)

app.config["SECRET_KEY"] = "Howdy D6"
if not uploadsdir.exists():
    uploadsdir.mkdir()
app.config["UPLOADED_PHOTOS_DEST"] = str(uploadsdir)

#REPLACE THIS WITH YOUR PERSONAL GOOGLE CLIENT ID TO TEST
GOOGLE_CLIENT_ID = ""
client_secrets_file  = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
os.environ["OAUTHLIB_INSECURE_TRANSPORT"]= "1"
flow = Flow.from_client_secrets_file(client_secrets_file=client_secrets_file,
        scopes = [ "https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
        redirect_uri = "http://127.0.0.1:5000/callback")   
def login_is_required(function):    #protect site by requiring login
    def wrapper(*args, **kwargs):   
        if "google_id" not in session:  #checks to see if google user is logged in
            return abort(401) #authorization required
        else:
            return function()
    return wrapper
@app.route("/" )
def get_start():
    return render_template("/login.html")
@app.route("/login", methods=["POST"])
def login():
    authorization_url, state = flow.authorization_url() #the state is a security feature, a random var that will be sent back from the authorization server.
    session["state"] = state
    return redirect(authorization_url)

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)      #state doesn't match
    
    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token = credentials._id_token,
        request = token_request, 
        audience = GOOGLE_CLIENT_ID
    )
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/home")

@app.route("/logout")
def logout():
    session.clear()     #clears logged session, google_id is erased.
    return redirect("/")

@app.route("/protected_area")
@login_is_required
def protected_area():
    return "protected! <a href='/logout'><button> Logout</button></a>"
@app.route("/home")
def get_home():
    return render_template("/home.html", items=Database.get_all())


@app.route("/books")
def get_books():
    return render_template(
        "/books.html", items=Database.get_item_by_category(Category.BOOK)
    )


@app.route("/clothes")
def get_clothes():
    return render_template(
        "/clothes.html", items=Database.get_item_by_category(Category.CLOTHING)
    )


@app.route("/electronics")
def get_electronics():
    return render_template(
        "/electronics.html", items=Database.get_item_by_category(Category.ELECTRONIC)
    )


@app.route("/sports")
def get_sports():
    return render_template(
        "/sports.html", items=Database.get_item_by_category(Category.SPORTS_GEAR)
    )


@app.route("/furniture")
def get_furniture():
    return render_template(
        "/furniture.html", items=Database.get_item_by_category(Category.FURNITURE)
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
        return render_template("/sell.html")
    return render_template("/sell.html")


@app.route("/view/<item_id>")
def get_view(item_id):
    item = Database.get_item_by_id(item_id)
    if isinstance(item, ClothingItem):
        return render_template(
            "/view.html",
            item=item,
            small=item.get_size() == 0,
            medium=item.get_size() == 1,
            large=item.get_size() == 2,
            xlarge=item.get_size() == 3,
            unisex=item.get_gender() == 0,
            female=item.get_gender() == 1,
            male=item.get_gender() == 2,
            clothing=True,
        )

    if isinstance(item, BookItem):
        return render_template("/view.html", item=item, book=True)

    if isinstance(item, FurnitureItem):
        return render_template("/view.html", item=item, furn=True)

    if isinstance(item, ElectronicItem):
        return render_template("/view.html", item=item, elect=True)

    if isinstance(item, SportsGearItem):
        return render_template(
            "/view.html",
            item=item,
            small=item.get_size() == 0,
            medium=item.get_size() == 1,
            large=item.get_size() == 2,
            xlarge=item.get_size() == 3,
            unisex=item.get_gender() == 0,
            female=item.get_gender() == 1,
            male=item.get_gender() == 2,
            sports=True,
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
        term = request.form["search_term"]
    return render_template("/results.html", items=Database.search_item(term))


if __name__ == "__main__":
    app.run(debug=True)
