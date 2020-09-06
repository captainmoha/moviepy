import requests

API_URL = 'https://ghibliapi.herokuapp.com'


def get_films():
    try:
        return requests.get(f'{API_URL}/films')

    except requests.ConnectionError as conn_err:
        print(conn_err)
        return []


def get_people():

    try:
        return requests.get(f'{API_URL}/people')
    except requests.ConnectionError as conn_err:
        print(conn_err)
        return []


def add_people_to_movies(films, people):
    # Ammends films dict with correct people in films 

    for film in films:
        film['people'] = []
        for person in people:
            person_films = person['films']
            # add person to film if he is in it
            film['people'].extend(
                [person for film_in in person_films if film_in == film['url']])

    return films


def get_movies_with_people_json():

    # get movies
    films_resp = get_films()
    films_json_list = films_resp.json() if not films_resp == [] else films_resp

    # get people
    people_resp = get_people()
    people_json_list = people_resp.json() if not people_resp == [] else people_resp

    movies_with_people = add_people_to_movies(
        films_json_list, people_json_list)

    return movies_with_people
