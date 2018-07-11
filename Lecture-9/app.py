from flask import Flask, request, render_template

from flask_peewee import db

from peewee import CharField

from users import users

app = Flask(__name__)

# http://localhost:8080/users/anuj


class User(db.Model):
    username = CharField(unique=True)
    name = CharField()
    hobby = CharField()


@app.route("/users/<name>")
def profile(name):

    user = User()
    user.name = users[name]["name"]
    user.hobby = users[name]["hobby"]



    return render_template("home.html", user=user)


@app.route("/")
def home():
    return "Hello world"


@app.route("/bhopal", methods=["POST"])
def login():
    print(request.form.get("email"))
    print(request.form.get("pwd"))
    return "Now you are login as " + request.form.get("email")


@app.after_request
def add_header(response):

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


app.run(port=8080, debug=True)

# codeshare.io/29VAjg



