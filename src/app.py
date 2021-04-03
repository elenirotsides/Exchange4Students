import os
from flask import Flask, render_template, url_for, request
from flask_pymongo import PyMongo
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import db as d #this needs to change, db should be the mongodb Eleni makes. This is just so I can write line 31

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Howdy D6'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads') # you'll need to create a folder named uploads

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    submit = SubmitField('Upload')

@app.route('/uploads', methods=['POST'])
def get_imgs():
    target = os.path.join(basedir, 'uploads')
    if not os.path.isdir(target):
        os.mkdir(target)                #makes a folder if one doesn't already exists
    img_db_table = d.mongo.db.images    # database table name
    if request.method == 'POST':
        for upload in request.files.getlist("uploads"): #multiple image handle
            filename = secure_filename(upload.filename)
            destination = "/".join([target, filename])
            upload.save(destination)
            img_db_table.insert({'uploads': filename})  #insert into database

        return 'Image Upload Succesful'


@app.route('/')
def get_home():
    return render_template('/home.html')


@app.route('/books')
def get_books():
    return render_template('/books.html')


@app.route('/clothes')
def get_clothes():
    return render_template('/clothes.html')


@app.route('/electronics')
def get_electronics():
    return render_template('/electronics.html')


@app.route('/sports')
def get_sports():
    return render_template('/sports.html')


@app.route('/furniture')
def get_furniture():
    return render_template('/furniture.html')

@app.route('/sell', methods=['GET', 'POST'])
def get_sell():
    print("howdy")
    if request.method == 'POST':
        price = request.form['price_val']
        quantity = request.form['quantity_val']
        title = request.form['title_val']
        edition = request.form['ed_val']
        height = request.form['height_val']
        length = request.form['length_val']
        print("hello")
        print(quantity)
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
