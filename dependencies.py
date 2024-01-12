import os
from fastapi import Header, HTTPException, Depends
from pymongo import MongoClient

async def get_toker_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    
async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
    
async def connect_db():
    if os.environ.get("FASTAPING_ENV") == "prod":
        myclient = MongoClient("mongodb://mongodb-svc:27017")
    elif os.environ.get("FASTAPING_ENV") == "dev":
        myclient = MongoClient("mongodb://localhost:29009")
    else:
        myclient = MongoClient("mongodb://localhost:29009")

    mydb = myclient["mydatabase"]
    return mydb["items"]

async def get_db(mycol = Depends(connect_db)):
    return mycol
