from flask import Flask

my_app = Flask("happy")


@my_app.route("")
def home():
    # return r'<a href="/bye">bye</a>'
    return r'<h1>Wow</h1>'


@my_app.route("/bye")
def hello():
    return "Good Bye this world"

my_app.run()