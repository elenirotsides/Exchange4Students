from flask import Flask, render_template
from e4stypes.database import Database

app = Flask(__name__)


@app.route('/')
def get_home():
    return render_template('/home.html', items=Database.get_all())


@app.route('/books')
def get_books():
    return render_template('/books.html', items=Database.get_item_by_category("Book"))


@app.route('/clothes')
def get_clothes():
    return render_template('/clothes.html', items=Database.get_item_by_category("Clothing"))


@app.route('/electronics')
def get_electronics():
    return render_template('/electronics.html', items=Database.get_item_by_category("Electronic"))


@app.route('/sports')
def get_sports():
    return render_template('/sports.html', items=Database.get_item_by_category("Sports Gear"))


@app.route('/furniture')
def get_furniture():
    return render_template('/furniture.html', items=Database.get_item_by_category("Furniture"))


@app.route('/sell')
def get_sell():
    return render_template('/sell.html')


@app.route('/view')
def get_view():
    return render_template('/view.html')


if __name__ == "__main__":
    app.run(debug=True)
