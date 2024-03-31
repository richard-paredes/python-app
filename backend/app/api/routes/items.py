from typing import List, Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Person(BaseModel):
    id: int
    name: str
    age: int
    
DB: List[Person] = [
    Person(id=1, name="Richard", age=25),
    Person(id=2, name="Diana", age=25)
]

@router.get("/")
def read_items():
    return DB

@router.get("/{item_id}")
def read_item(item_id: int, q:Optional[str] = None):
    def search(id: int):
        matched = [i for i in DB if i.id == id]
        if len(matched) == 0:
            return None
        return matched[0]
    return search(item_id)
