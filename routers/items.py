from fastapi import APIRouter, Depends, HTTPException, Path
from typing import Annotated, Any
from dependencies import get_query_token, get_toker_header, get_db
from pydantic import BaseModel
from pymongo import MongoClient

router = APIRouter(
    prefix="/items",
    tags=["itmes"],
    #dependencies=[Depends(get_toker_header)],
    responses={404: {"description": "Not found"}},
)

class Item(BaseModel):
    name: str
    description: str | None
    price: float
    tax: float | None = None

@router.get("/")
async def read_items(mycol = Depends(get_db)):
    result = mycol.find({}, {"_id": 0});
    #这里不能直接返回查询结果，是因为find()查出来的是一个游标，而不是一个具本dict属性的(文档)对象，但是find_one()查出来的不是游标而且一个文档对象
    items = [Item(name=item["name"], description=item["description"],price=item["price"],tax=item["tax"]) for item in result]
    if result is not None:
        return items
    else:
        return "no data"

@router.get("/{item_id}")
async def read_item(item_id: str, mycol = Depends(get_db)):
    myquery = {"name": item_id}
    x = mycol.find_one(myquery, {"_id": 0})
    if x is not None:
        return x
    else:
        return "no such items"
   
@router.put( "/{item_id}")
async def update_item(item_id: str, item: Item, mycol = Depends(get_db)):
    myquery = {"name":item_id}
    result = mycol.update_one(myquery, {"$set":item.dict()})
    if result.matched_count > 0:
        return item
    else:
        return "no such items"

@router.post("/addUser", status_code=201, response_model=Item)
async def add_user(item : Item, mycol = Depends(get_db)) -> Any:
    mycol.insert_one(item.dict())
    return item

@router.delete("/{item_id}")
async def delete_user(item_id: str, mycol = Depends(get_db)):
    myquery = {"name": item_id}
    result = mycol.delete_one(myquery)
    if result.deleted_count > 0:
        return "deleted successfully"
    else:
        return "no such items"

