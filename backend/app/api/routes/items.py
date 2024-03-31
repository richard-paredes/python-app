from typing import List
from http import HTTPStatus
from fastapi import APIRouter, HTTPException

from backend.app.models import Person, PersonBase

router = APIRouter()

DB: List[Person] = [
    Person(id=1, name="Richard", age=25),
    Person(id=2, name="Diana", age=25)
]

@router.get("/")
def read_items():
    return DB

@router.get("/{item_id}", status_code=HTTPStatus.OK)
def read_item(item_id: int):
    def search(id: int):
        matched = [i for i in DB if i.id == id]
        if len(matched) == 0:
            return None
        return matched[0]
    
    item = search(item_id)
    if not item: raise HTTPException(HTTPStatus.NOT_FOUND, detail="Item not found")
    return item

@router.post("/", status_code=HTTPStatus.CREATED)
def create_item(item_create: PersonBase):
    new_person = Person.model_validate(item_create, update={"id":len(DB)})
    DB.append(new_person)
    return new_person
