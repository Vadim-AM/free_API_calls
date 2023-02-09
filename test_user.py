import requests

import config
from src.generators.user import User
from src.schemas.userschema import UserSchema


class TestUsers:

    def test_user_schema(self):
        r = requests.get(config.USERS_URL)
        assert r.status_code == 200
        for user in r.json().get('data'):
            assert UserSchema.parse_obj(user)

    def test_user_create_w_company(self, user: User):
        user = user.set_last_name().user
        r = requests.post(config.USERS_URL, json=user)
        assert r.status_code == 201, r.json()
        assert UserSchema.parse_obj(r.json())
