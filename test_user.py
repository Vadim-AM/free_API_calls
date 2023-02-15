from time import sleep

import pytest
import requests

import config
from src.generators.user import user_wo_last_name, user_inactive_company, positive_user_cases
from src.schemas.userschema import UserSchema


class TestUsers:

    def test_user_schema(self):
        r = requests.get(config.USERS_URL)
        assert r.status_code == 200
        for user in r.json().get('data'):
            assert UserSchema.parse_obj(user)
            print(user)

    @pytest.mark.parametrize('field', positive_user_cases)
    def test_user_create_positive(self, user, field: dict):
        user = user.add_fields(field)
        r = requests.post(config.USERS_URL, json=user)
        assert r.status_code == 201, r.json()
        assert UserSchema.parse_obj(r.json())

    def test_user_create_wo_last_name(self, user):
        user = user.add_fields(user_wo_last_name)
        r = requests.post(config.USERS_URL, json=user)
        assert r.status_code == 422, r.json()['detail']
        assert UserSchema.parse_obj(r.json())

    def test_user_create_inactive_company(self, user):
        user = user.add_fields(user_inactive_company)
        r = requests.post(config.USERS_URL, json=user)
        assert r.status_code == 400, r.json()['detail']
        assert UserSchema.parse_obj(r.json())

    def test_user_id(self, user):
        user = user.add_fields({'last_name': 'Unique_Name', 'user_id': 2465})
        r = requests.post(config.USERS_URL, json=user)
        assert r.status_code == 201, r.json()
        print(user.get("user_id"))
        sleep(1)
        get_user = requests.get(f'{config.USERS_URL}2465')
        print(get_user.json())
        assert get_user.status_code == 200, get_user.json()
