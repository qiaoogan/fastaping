import os
from fastapi import Header, HTTPException, Depends
from pymongo import MongoClient
from functools import partial

async def get_toker_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    
async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
    
async def connect_db(collection_name: str):
    if os.environ.get("FASTAPING_ENV") == "prod":
        myclient = MongoClient("mongodb://mongodb-svc:27017")
    elif os.environ.get("FASTAPING_ENV") == "dev":
        myclient = MongoClient("mongodb://localhost:29009")
    else:
        myclient = MongoClient("mongodb://localhost:29009")

    mydb = myclient["mydatabase"]
    return mydb[collection_name]


# async def get_db(mycol = Depends(connect_db)):
#     return mycol


def get_db(collection_name: str):
    async def _get_db():
        return await connect_db(collection_name)
    return _get_db  