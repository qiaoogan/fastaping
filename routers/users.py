from fastapi import APIRouter, Depends
from dependencies import get_db
from pydantic import BaseModel
from typing import Annotated, Any

router = APIRouter()

class User(BaseModel):
    account: str
    password: str
    publishedAt: str
    price: float
    stock: int

@router.get("/users/", tags=["users"])
async def read_users(mycol=Depends(get_db(collection_name="users"))):
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/users/{username}", tags=["users"])
async def read_user(username:str):
    return {"username", username}

@router.post("/", status_code=201, response_model=User)
async def add_user(user : User, mycol=Depends(get_db(collection_name="users"))) -> Any:
    mycol.insert_one(user.dict())
    return user