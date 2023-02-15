from pydantic import BaseModel

from src.enums.company_enum import Statuses


class CompanySchema(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: Statuses
