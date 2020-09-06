from flask import Blueprint, jsonify
from flasgger import swag_from

from app.services import ghibli

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/movies/')
@swag_from('../docs/swagger/movies.yml')
def get_movies_json():
    movies_json = ghibli.get_movies_with_people_json()

    if len(movies_json) == 0:
        return jsonify(movies_json), 400

    return jsonify(movies_json), 200
