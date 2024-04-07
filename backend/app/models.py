from sqlmodel import SQLModel, Field

class PersonBase(SQLModel):
    name: str
    age: int

class Person(PersonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class PersonOut(PersonBase):
    id: int