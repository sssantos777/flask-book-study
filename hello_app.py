from flask import Flask

app = Flask(import_name=__name__)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


"""
OR
def index(): <- This is a view function
    return "<h1>Hello World!</h1>"
app.add_url_rule("/", "index", index)
"""


# Route with a dynamic component
@app.route("/user/<name>")  # ex: /user/arthur
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

# You can use different type of data like /user/<int:id>. ex: /user/213

# Run on linux
# (venv) $ export FLASK_APP=hello_app.py
# (venv) $ flask run


"""
To use venv -> 
installing --
$ sudo apt-get install python3-venv
# $ python -m venv <virtual-environment-name> <- commonly called venv
$ python -m venv ven
using --
$ source venv/bin/activate
"""
