import os
from decimal import Decimal
from flask import Flask, render_template, request, redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from werkzeug.utils import secure_filename
from e4stypes.database import Database
from e4stypes.book_item import BookItem
from e4stypes.clothing_item import ClothingItem
from e4stypes.electronic_item import ElectronicItem
from e4stypes.furniture_item import FurnitureItem
from e4stypes.sports_gear_item import SportsGearItem

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Howdy D6'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(
    basedir, 'uploads')  # you'll need to create a folder named uploads

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileAllowed(photos, 'Image only!'),
        FileRequired('File was empty!')
    ])
    submit = SubmitField('Upload')


# commenting out for pylint
# @app.route('/uploads', methods=['POST'])
# def get_imgs():
#     target = os.path.join(basedir, 'uploads')
#     if not os.path.isdir(target):
#         os.mkdir(target)  #makes a folder if one doesn't already exists
#     img_db_table = Database.mongo.db.images  # database table name
#     if request.method == 'POST':
#         for upload in request.files.getlist("uploads"):  #multiple image handle
#             filename = secure_filename(upload.filename)
#             destination = "/".join([target, filename])
#             upload.save(destination)
#             img_db_table.insert({'uploads': filename})  #insert into database

#         return 'Image Upload Succesful'
#     return 'None'


@app.route('/')
def get_home():
    return render_template('/home.html', items=Database.get_all())


@app.route('/books')
def get_books():
    return render_template('/books.html',
                           items=Database.get_item_by_category("Book"))


@app.route('/clothes')
def get_clothes():
    return render_template('/clothes.html',
                           items=Database.get_item_by_category("Clothing"))


@app.route('/electronics')
def get_electronics():
    return render_template('/electronics.html',
                           items=Database.get_item_by_category("Electronic"))


@app.route('/sports')
def get_sports():
    return render_template('/sports.html',
                           items=Database.get_item_by_category("Sports Gear"))


@app.route('/furniture')
def get_furniture():
    return render_template('/furniture.html',
                           items=Database.get_item_by_category("Furniture"))


@app.route('/sell', methods=['GET', 'POST'])
def get_sell():
    if request.method == 'POST':
        #grab form data in order they appear in sell.html
        category = request.form['category_drop_val']
        post_title = request.form['post_title_val']
        price = request.form['price_val']
        title = request.form['title_val']
        edition = request.form['ed_val']
        dimensions = [
            int(request.form['length_val']),
            int(request.form['width_val']),
            int(request.form['height_val'])
        ]
        weight = request.form['weight_val']
        color = request.form['color_val']
        #type is a key word
        type_val = request.form['type_val']
        course_num = request.form['course_num_val']
        size = request.form['size_val']
        gender = request.form['gender_val']
        model = request.form['model_val']
        description = request.form['comments_val']
        seller = request.form['seller_val']

        # create item and add item to database
        if category == 'books':
            Database.add_item(
                BookItem(post_title, description, Decimal(price.strip()),
                         float(weight.strip()), seller, title, edition,
                         course_num))
        elif category == 'furniture':
            Database.add_item(
                FurnitureItem(post_title, description, Decimal(price.strip()),
                              float(weight.strip()), seller, type_val, color,
                              dimensions))
        elif category == 'clothes':
            Database.add_item(
                ClothingItem(post_title, description, Decimal(price.strip()),
                             float(weight.strip()), seller, type_val, size,
                             gender, color))
        elif category == 'sports':
            Database.add_item(
                SportsGearItem(post_title, description, Decimal(price.strip()),
                               float(weight.strip()), seller, type_val, size,
                               gender))
        elif category == 'electronics':
            Database.add_item(
                ElectronicItem(post_title, description, Decimal(price.strip()),
                               float(weight.strip()), seller, type_val, model,
                               dimensions))
        return redirect('/photosub')

    return render_template('/sell.html')


@app.route('/photosub', methods=['GET', 'POST'])
def get_photosub():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
    else:
        file_url = None
    return render_template('/photosub.html', form=form, file_url=file_url)


@app.route('/view')
def get_view():
    return render_template('/view.html')


if __name__ == "__main__":
    app.run(debug=True)
