from fastapi import FastAPI, HTTPException
from typing import Optional,List
from pydantic import BaseModel

from model import User , Gender, Roles, UserUpdateRequest
from uuid import UUID, uuid4

app = FastAPI()

db : List[User] = [

    User(
        id = uuid4(),
        first_name = "Hema",
        last_name = "Chandran",
        gender = Gender.male,
        role = [Roles.admin, Roles.user]
    ),
    User(
        id = uuid4(),
        first_name = "Hitesh",
        last_name = "S",
        gender = Gender.male,
        role = [Roles.admin, Roles.user]

    )
]
@app.get("/api/users")
def users():
    return db

@app.post("/api/users")
def users(user:User):
    db.append(user)
    return {"id": user.id}

@app.put("/api/users/{user_id}")
def updateUser(user_update:UserUpdateRequest,user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.role is not None:
                user.role = user_update.role
            return 
    raise HTTPException(
        status_code=404,
        details = f"User with id: {user_id} does not exists"
    )

# @app.get("/index/{name}")
# def index(name):
#     return f"welcome to my port {name}"



# @app.get("/user/{id}")
# def user(id:int, limit:int = 10):
#     return {"data":{"id": id, "limit":limit}}

# @app.get("/user_1/{id}")
# def user_1(id:int , limit:Optional[int] = None):
#     return {"data":{"id":id, "limit":limit}}

# @app.get("/user_2/{id}")
# def user_1(id:int , limit:Optional[int] = None):

#     if limit is None:
#         return {"data":{"id":id}}
#     else:
#         return {"data":{"id":id, "limit":limit}}
    



# # -------------
# class Request(BaseModel):

#     name: str
#     age: int
#     email: str




# @app.post("/")
# def index(request:Request):
#     return { "data" : request}


# ----------------CRED Operation


    