import pytest
import requests

import config
from src.enums.company_enum import Statuses
from src.schemas.company import Company


class TestCompanies:

    def test_companies_response_and_schema(self):
        r = requests.get(f'{config.COMPANIES_URL}?limit=999')
        assert r.status_code == 200
        for i in r.json()['data']:
            assert Company.parse_obj(i)

    @pytest.mark.parametrize('status', Statuses)
    def test_companies_status(self, status: str):
        stat = status.__str__().split('.')[1]
        r = requests.get(f'{config.COMPANIES_URL}?status={stat}&limit=10')
        assert r.status_code == 200
        for i in r.json()['data']:
            assert Company.parse_obj(i).company_status == status

    @pytest.mark.parametrize('limit, offset, result', [('3', '7', 0), ('7', '3', 4), ('0', '0', 0)])
    def test_companies_search_limit_offset(self, limit: str, offset: str, result: int):
        r = requests.get(f'{config.COMPANIES_URL}?limit={limit}&offset={offset}')
        assert len(r.json()['data']) <= int(limit)
        if len(r.json()['data']) > 0:
            assert r.json()['data'][0]['company_id'] == result

    @pytest.mark.parametrize('comp_id', ['1', '7'])
    def test_company_on_id(self, comp_id: str):
        r = requests.get(f'{config.COMPANIES_URL}{comp_id}')
        assert r.json()['company_id'] == int(comp_id)

    def test_company_on_id_negative(self):
        r = requests.get(f'{config.COMPANIES_URL}{str(0)}')
        assert r.status_code == 404
        assert r.json().get('detail')
