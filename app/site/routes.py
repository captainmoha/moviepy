from flask import Blueprint, jsonify, render_template, redirect

from app.services import ghibli
from app.services.cache import cache

site = Blueprint('site', __name__, template_folder='templates')


@site.route('/movies/')
@cache.cached(timeout=60)  # cache results for 1 minute
def get_movies():
    movies = ghibli.get_movies_with_people_json()

    return render_template('base.html', movies=movies)

@site.route('/')
def index():
    return redirect('/movies/')