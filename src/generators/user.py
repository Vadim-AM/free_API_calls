from faker import Faker

fake = Faker()


class User:

    def __init__(self) -> None:
        self.user = {}

    def add_fields(self, fields):
        if not isinstance(fields, dict):
            self.user = fields
        else:
            for field, value in fields.items():
                self.user[field] = value
        return self.user


positive_user_cases = [
    {
        'last_name': fake.name().split()[1],
        'company_id': 1,
        'user_id': fake.random.randint(1, 999)
    },
    {
        'last_name': fake.name().split()[1],
        'first_name': fake.name().split()[0],
        'user_id': fake.random.randint(1, 999)
    },
    {
        'last_name': fake.name().split()[1],
        'first_name': fake.name().split()[0],
        'company_id': 2

    },
    {
        'first_name': fake.name().split()[0],
        'last_name': fake.name().split()[1],
        'company_id': 3
    }
]

user_wo_last_name = {
    'last_name': fake.name().split()[1],
    'company_id': 0,
    'user_id': fake.random.randint(1, 999)
}
user_inactive_company = {
    'first_name': fake.name().split()[0],
    'company_id': 7,
    'user_id': fake.random.randint(1, 999)
}
