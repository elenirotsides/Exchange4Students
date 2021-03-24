from flask import Flask, render_template
app = Flask(__name__)

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

@app.route('/sell')
def get_sell():
    return render_template('/sell.html')

@app.route('/view')
def get_view():
    return render_template('/view.html')



if __name__ == "__main__":
    app.run(debug=True)
