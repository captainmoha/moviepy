from flask import Blueprint, jsonify, render_template

from app.services import ghibli

site = Blueprint('site', __name__, template_folder='templates')


@site.route('/movies/')
def get_movies():
    movies = ghibli.get_movies_with_people_json()

    return render_template('base.html', movies=movies)
