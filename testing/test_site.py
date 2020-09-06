import json


def test_get_movies(app, client):

    res = client.get('/movies/')

    assert res.status_code == 200

    expected = {'ghibli': 'movies'}

    assert json.loads(res.get_data()) == expected
