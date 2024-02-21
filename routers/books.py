from fastapi import APIRouter, Depends, HTTPException, Path
from typing import Annotated, Any
from dependencies import get_query_token, get_toker_header, get_db
from pydantic import BaseModel
from datetime import date


# 库存服务
# 实现如下接口：
# ```
# /stock/book, GET ---> 查询books的数据；
# /stock/book, POST ---> 创建单个book的数据；
# /stock/book, DELETE ---> 删除单个book的数据；
# /stock/book, PUT ---> 更新单个book的数据；


router = APIRouter(
    prefix="/stock/book",
    tags=["books"],
    #dependencies=[Depends(get_toker_header)],
    responses={404: {"description": "Not found"}},
)

class Book(BaseModel):
    name: str
    author: str
    publishedAt: str
    price: float
    stock: int


#get_db_with_collection = partial(get_db, collection_name="items")  

@router.get("/")
async def get_all_books(mycol=Depends(get_db(collection_name="books"))):
    result = mycol.find({}, {"_id": 0});
    #这里不能直接返回查询结果，是因为find()查出来的是一个游标，而不是一个具本dict属性的(文档)对象，但是find_one()查出来的不是游标而且一个文档对象
    books = [Book(name=book["name"], author=book["author"],publishedAt=book["publishedAt"],price=book["price"],stock=book["stock"]) for book in result]
    print(books)
    if result is not None:
        return books
    else:
        return "no data"

@router.get("/{book_name}")
async def read_book(book_name: str, mycol=Depends(get_db(collection_name="books"))):
    myquery = {"name": book_name}
    x = mycol.find_one(myquery, {"_id": 0})
    if x is not None:
        return x
    else:
        return "no such book"
   
@router.put( "/{book_name}")
async def update_book(book_name: str, book: Book, mycol=Depends(get_db(collection_name="books"))):
    myquery = {"name":book_name}
    result = mycol.update_one(myquery, {"$set":book.dict()})
    if result.matched_count > 0:
        return book
    else: 
        return "no such items"

@router.post("/", status_code=201, response_model=Book)
async def add_book(book : Book, mycol=Depends(get_db(collection_name="books"))) -> Any:
    mycol.insert_one(book.dict())
    return book

@router.delete("/{book_name}")
async def delete_user(book_name: str, mycol=Depends(get_db(collection_name="books"))):
    myquery = {"name": book_name}
    result = mycol.delete_one(myquery)
    if result.deleted_count > 0:
        return "deleted successfully"
    else:
        return "no such book"

