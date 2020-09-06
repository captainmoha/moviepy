from flask import Blueprint, jsonify

site = Blueprint('site', __name__)


@site.route('/movies/')
def get_movies():
    return jsonify({'ghibli': 'movies'})
