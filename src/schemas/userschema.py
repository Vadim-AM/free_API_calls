from pydantic import BaseModel


class UserSchema(BaseModel):
    first_name: str | None
    last_name: str | None
    company_id: int | None
    user_id: int | None
