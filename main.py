from src import create_app

app = create_app()

# @app.route('/')
# def hello():
#     return "HELLOWWWW"
if __name__ == '__main__':
    app.run(debug=True)