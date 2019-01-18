from flask import Blueprint, jsonify


mod_api = Blueprint('api', __name__)

@mod_api.route('/')
def index():
    return jsonify({"message": "index"})
