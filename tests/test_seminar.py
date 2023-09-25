"""
Задание 1.
Добавить в задание с REST API еще один тест, в котором создается новый пост, а потом проверяется его наличие на сервере
по полю “описание”.
"""

import requests
import yaml

from bin.api_utils import check_text

with open('config/config.yaml', 'rb') as f:
    data = yaml.safe_load(f)


def test_step1(valid_word, invalid_word):
    assert valid_word in check_text(invalid_word), 'test_step1 FAIL'


def test_step2(user_login, post_title):
    result = requests.get(url=data['api'], headers={'x-auth-token': user_login}, params={'owner': 'notMe'}).json()[
        'data']
    result_title = [i['title'] for i in result]
    assert post_title in result_title, 'test 2 FAIL'

#Домашнее Задание №1
def test_step3(user_login, create_post):
    res = []
    res.append(True) if create_post == 200 else False
    result = requests.get(url=data['api'], headers={'x-auth-token': user_login}, params={'owner': 'Me'}).json()[
        'data']
    result_title = [i['title'] for i in result]
    res.append(True) if data['title'] in result_title else False
    assert all(res)
