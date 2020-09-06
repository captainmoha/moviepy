from flask import Blueprint, jsonify

from app.services import ghibli


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/movies/')
def get_movies_json():

    return jsonify(ghibli.get_movies_with_people_json())
