from app.services import ghibli
import requests

from unittest.mock import patch, Mock


fake_movies_with_people = [
    {
        'id': 'fakemovieid1',
        'people': [
            {'id': 'personid1', 'name': 'totoro'}, {
                'id': 'personid2', 'name': 'shishigami'}
        ]
    },
    {
        'id': 'fakemovieid2',
        'people': [
            {'id': 'personid3', 'name': 'yuki'}, {
                'id': 'personid4', 'name': 'haru'}
        ]
    },
]


def fake_films_json():
    return [
        {
            "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "title": "Castle in the Sky",
        },
        {
            "id": "12cfb892-aac0-4c5b-94af-521852e46d6a",
            "title": "Grave of the Fireflies",
        }
    ]


def fake_people_json():
    return [
        {
            "id": "fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
            "name": "Pazu",
            "films": [
                "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
            ],
        },
        {
            "id": "598f7048-74ff-41e0-92ef-87dc1ad980a9",
            "name": "Lusheeta Toel Ul Laputa",
            "films": [
                "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
            ],
        }
    ]


@patch('requests.get')
def test_get_films(mocked_get):

    mocked_get.return_value = Mock(
        ok=True, status_code=200, json=fake_films_json)
    films_resp = ghibli.get_films()

    assert films_resp.ok

    films_json = films_resp.json()

    assert len(films_json) > 0
    assert type(films_json[0]) == dict


@patch('requests.get')
def test_get_films_api_fail(mocked_get):

    mocked_get.return_value = Mock(ok=False, status_code=404, json=lambda: [])
    films_resp = ghibli.get_films()
    assert not films_resp.ok
    assert len(films_resp.json()) == 0


@patch('requests.get')
def test_get_people(mocked_get):

    mocked_get.return_value = Mock(
        ok=True, status_code=200, json=fake_people_json)

    people_resp = ghibli.get_people()

    assert people_resp.ok

    people_json = people_resp.json()

    assert len(people_json) > 0
    assert type(people_json[0]) == dict


@patch('app.services.ghibli.add_people_to_movies')
def test_get_movies_with_people_json(mocked_add_people_to_movies):

    mocked_add_people_to_movies.return_value = fake_movies_with_people
    movies_with_people = ghibli.get_movies_with_people_json()

    assert len(movies_with_people) > 1
    assert type(movies_with_people[0]) == dict
    assert len(movies_with_people[0]['people']) > 0
