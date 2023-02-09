import random

from faker import Faker


class User:

    def __init__(self) -> None:
        self.user = {}
        self.__fake = Faker()

    def set_first_name(self):
        self.user['first_name'] = self.__fake.name().split()[0]
        return self

    def set_last_name(self):
        self.user['last_name'] = self.__fake.name().split()[1]
        return self

    def set_company_id(self, company_ids: list):
        self.user['company_id'] = random.choice(company_ids)
        return self

    def set_user_id(self):
        self.user['user_id'] = self.__fake.random.randint(0, 99)

    def user(self):
        return self.user
