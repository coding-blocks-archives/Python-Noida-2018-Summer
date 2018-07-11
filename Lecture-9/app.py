from flask import Flask, request, render_template

app = Flask(__name__)

# http://localhost:8080/users/anuj

@app.route("/users/<name>")
def users(name):
    return "Hello " + name


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


