import pytest
import requests

import config
from src.generators.user import User


@pytest.fixture
def user():
    """
    The fixture passes an object without call which
    generate user in test function when called
    """
    return User()


@pytest.fixture()
def active_company_ids():
    """
    returns ids of companies with "ACTIVE" status
    """
    r = requests.get(config.COMPANIES_URL)
    active_ids = []
    for company in r.json()['data']:
        active_ids.append(company.company_id)
    return active_ids
