from flask import Blueprint


login = Blueprint('login', __name__)


@login.route('/')
def index():
    return "Login"