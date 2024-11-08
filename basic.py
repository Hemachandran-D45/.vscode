from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

#FastApi : A web framework for building APIs quickly and efficiently.
#BaseModel: Part of Pydantic, it helps validate and serialize request/response data.
# Optional : Typing hints for optional and list data types.

app = FastAPI() 


#Route Creation
@app.get("/index/{name}")
def index(name): #name is path parameter
    return f"welcome to my port {name}"


@app.get("/user/{id}")
def user(id:int, limit:int = 10): #in default I mention as 10 if we give any other integer it will print that or 
#                                     take 10 as defalut
    return {"data":{"id": id, "limit":limit}}


@app.get("/user_1/{id}") #limit parameter as optional
def user_1(id:int , limit:Optional[int] = None):
    return {"data":{"id":id, "limit":limit}}


@app.get("/user_2/{id}")
def user_1(id:int , limit:Optional[int] = None):

    if limit is None:
        return {"data":{"id":id}}
    else:
        return {"data":{"id":id, "limit":limit}}
    

class Request(BaseModel):

    name: str
    age: int
    email: str




@app.post("/")
def index(request:Request):
    return { "data" : request}



    