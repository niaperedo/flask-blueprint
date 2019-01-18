from flask import Blueprint


mod_web = Blueprint('web', __name__)

@mod_web.route('/')
def index():
    return '<h1>Index</h1>'
