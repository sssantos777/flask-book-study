from flask import Flask, request, make_response

app = Flask(import_name=__name__)


@app.route("/browser/")
def browser():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your browser is: <b>{}</b></p>".format(user_agent)


@app.route("/bad_request/")
def bad_req_response():
    return "<h1>Bad Request.</h1>", 400


@app.route("/response_object/")
def response_object():
    response = make_response("<h1>This document carries a cookie.</h1>")
    response.set_cookie("answer", "42")
    return response


from flask import redirect, abort


@app.route("/redirect/")
def redirect_func():
    return redirect("https://google.com")


@app.route("/abort/")
def abort_func():
    abort(404)


"""
#    Book Example
    @app.route('/user/<id>')
    def get_user(id):
        user = load_user(id)
        if not user:
            abort(404)
        return '<h1>Hello, {}</h1>'.format(user.name)
"""
