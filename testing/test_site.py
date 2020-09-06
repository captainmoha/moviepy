import json


def test_get_movies(app, client):

    # tests movies view html
    res = client.get('/movies/')

    assert res.status_code == 200
    assert 'text/html' in res.headers['content-type']
    assert int(res.headers['content-length']) > 0
