from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return render_template("index.html")


@auth.route('/signup')
def reg():
    return render_template("signup.html")


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/feedback')
def feedback():
    return render_template("feedback.html")
