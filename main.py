from fastapi import FastAPI, Depends
from dependencies import get_query_token, get_toker_header
from routers import items, users

from fastapi.staticfiles import StaticFiles

app = FastAPI(dependencsies=[Depends(get_toker_header)])
app.mount("/internal", StaticFiles(directory="internal"), name="admin.py")
#app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Application!"}