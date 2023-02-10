from faker import Faker


class User:

    def __init__(self) -> None:
        self.user = {}
        self.fake = Faker()

    def add_fields(self, fields):
        self.user['last_name'] = self.fake.name().split()[1]
        for field, value in fields.items():
            self.user[field] = value
        return self.user


def user_fields():
    fake = Faker()
    fields = [
        {
            'company_id': 1,
            'user_id': fake.random.randint(1, 999)
        },
        {
            'first_name': fake.name().split()[0],
            'user_id': fake.random.randint(1, 999)
        },
        {
            'first_name': fake.name().split()[0],
            'company_id': 1,
        }
    ]
    return fields
