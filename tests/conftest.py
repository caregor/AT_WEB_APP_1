import pytest
import requests
import yaml

with open('config/config.yaml', 'rb') as f:
    data = yaml.safe_load(f)

s = requests.Session()


@pytest.fixture()
def user_login():
    result = s.post(url=data['url'], data={'username': data['login'], 'password': data['password']})
    response_json = result.json()['token']
    return response_json


@pytest.fixture()
def post_title():
    return 'New Post'


@pytest.fixture()
def valid_word():
    return 'молоко'


@pytest.fixture()
def invalid_word():
    return 'малоко'


@pytest.fixture()
def create_post(user_login):

    result = s.post(url=data['api'], headers={'X-Auth-Token': user_login},
                    data={'title': data['title'], 'description': 'Some desciption', 'content': 'CONTENT'})
    return result.status_code,
