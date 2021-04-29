import flask
from flask import session, abort
import functools


def login_is_required(function):  # protect site by requiring login
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if "google_id" not in flask.session:  # checks to see if google user is logged in
            return abort(401)  # authorization required
        else:
            return function()

    return wrapper