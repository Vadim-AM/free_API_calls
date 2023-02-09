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
