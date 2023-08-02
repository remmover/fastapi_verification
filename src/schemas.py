from pydantic import BaseModel, Field
from datetime import date


class ContactSchema(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    surname: str = Field(min_length=2, max_length=50)
    email: str
    number: str | None
    bd_date: date
    additional_data: str | None = Field(max_length=300)


class ContactResponse(ContactSchema):
    id: int

    class Config:
        from_attributes = True
