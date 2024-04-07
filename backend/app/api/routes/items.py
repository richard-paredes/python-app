from typing import List
from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.models import Person, PersonCreate
from app.api.deps import SessionDep

router = APIRouter()

DB: List[Person] = [
    Person(id=1, name="Richard", age=25),
    Person(id=2, name="Diana", age=25)
]

@router.get("/")
def read_items(session: SessionDep):
    people = session.exec(select(Person)).all()
    return people

@router.get("/{item_id}", status_code=HTTPStatus.OK)
def read_item(item_id: int, session: SessionDep):
    def search(id: int):
        person = session.exec(select(Person).where(Person.id == id)).first()
        return person
    
    item = search(item_id)
    if not item: raise HTTPException(HTTPStatus.NOT_FOUND, detail="Person not found")
    return item

@router.post("/", status_code=HTTPStatus.CREATED)
def create_item(item_create: PersonCreate):
    new_person = Person.model_validate(item_create, update={"id":len(DB)})
    DB.append(new_person)
    return new_person
