import os
from fastapi import FastAPI, Depends
from dependencies import get_query_token, get_toker_header
from routers import items, users,books
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(dependencsies=[Depends(get_toker_header)])
app.mount("/internal", StaticFiles(directory="internal"), name="admin.py")
#app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 设置允许的来源，例如：["http://localhost", "http://localhost:8080"]
    allow_credentials=True,  # 是否允许发送凭据（例如 Cookie）
    allow_methods=["*"],  # 允许的 HTTP 方法，例如：["GET", "POST", "PUT", "DELETE"]
    allow_headers=["*"],  # 允许的自定义头部
)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(books.router)

@app.get("/health")
async def health():
    return {
        "alive": True,
        "version": os.environ.get("FASTAPING_VERSION")
    }