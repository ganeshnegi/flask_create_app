from flask import Blueprint

bp_home = Blueprint('home', __name__)

@bp_home.route('/')
def index():
	return "hello"