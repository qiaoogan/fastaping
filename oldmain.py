from fastapi import FastAPI, HTTPException, Query, Path, Body, Header, Form, File, UploadFile
from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from typing import Union, List,Annotated, Any


app = FastAPI()

class Item(BaseModel):
    name: str = Field(example="foo")
    description: str | None = Field(default=None, titile="This is a yield data", max_length=25)
    price: float
    tax: float | None = None
    
    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2,
    #             }
    #         ]
    #     }
    # }
    
class User(BaseModel):
    username: str
    full_name: str | None = None   
    
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None
    
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5},
}

@app.get('/items/{item_id}', tags=["get item"])
def get_item(item_id : str):
    if item_id not in items:
        raise HTTPException(status_code=404, 
                            detail=f"{item_id} not found",
                            headers={"X-Error": "There goes my error"}, )
    return items[item_id]

@app.get('/items', tags=['get all items'])
def get_all_items():
    return items

@app.put('/items/{item_id}', tags=["Multi-parameters"])
def update_item(item_id: int, item: Annotated[Item, Body(embed=True)], user: User, important: Annotated[int, Body()], user_agent: Annotated[str | None, Header()] = None):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

@app.delete('/items/{item_id}')
def delete_item(item_id: str):
    del items[item_id]
    return items

@app.get('/datacheck/{id}')
def check_data_type(id: int = Path(title="This is a path paramter", ge=3, le=30)):
    return {"int_data": id}

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = "resnet"
    lenet = 'lenet'
    
@app.get('/models')
def get_parameter(skip: int = 0, limit: int = 10):
    items[skip] = limit
    return items
    
    
@app.get('/models/{model_name}')
def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    elif model_name is ModelName.resnet:
        return {"model_name": model_name, "message": "LeCNN all the images"}
    else:
        return {"model_name": model_name, "message": "Have some residuals"}

@app.post('/basemodel')
async def create_model(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.get('/query/')
async def read_query_parameter(q: Union[str, None] = Query(default=..., min_length=3, max_length=10, pattern='^testing$')):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"items": q})
    return results 

@app.get('/queryList/')
async def read_list(q: Union[List[str], None] = Query(default=["foo","bar"])):
    return q 

@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights

@app.post("/responsemode/", response_model=List[Item], tags=["Response Mode"])
async def create_responsem(item: List[Item]) ->Any:
    return item

@app.post("/responseOut/", response_model=UserOut, tags=["Response Model"], status_code=201)
async def create_responseout(user: UserIn) -> Any:
    return user

@app.post("/login/")
async def login(username: str = Form(), passwork: str = Form()):
    return {"username": username}

@app.post("/files/")
async def create_file(file: bytes | None = File(default=None, description="A bytes file")):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = File(default=None, description="A uploaded file")):
    content = await file.read()
    return {"filename": file.filename, "content_type": file.content_type, "file": content}