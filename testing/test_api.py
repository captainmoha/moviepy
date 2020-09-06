import json


def test_api_get_movies(app, client):

    res = client.get('/api/movies/')

    assert res.status_code == 200

    movies_json = json.loads(res.get_data())

    assert len(movies_json) > 0
    assert type(movies_json[0]) == dict
    assert len(movies_json[0]['people']) > 0
