import pytest
import requests

import config
from src.generators.user import user_fields
from src.schemas.userschema import UserSchema


class TestUsers:

    def test_user_schema(self):
        r = requests.get(config.USERS_URL)
        assert r.status_code == 200
        for user in r.json().get('data'):
            assert UserSchema.parse_obj(user)

    @pytest.mark.parametrize('field', user_fields())
    def test_user_create(self, user, field: dict):
        user = user.add_fields(field)
        r = requests.post(config.USERS_URL, json=user)
        assert r.status_code == 201, r.json()
        print(user)
        assert UserSchema.parse_obj(r.json())
