from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


class User(BaseModel):
    username: str
    age: int
    message: str


@app.get("/user")
async def users_list():
    return users


@app.post("/user/")
async def user_add(user: User):
    next_index = str(int(max(users.keys(), key=int)) + 1)
    users[next_index] = f"Имя: {user.username}, возраст: {user.age}, сообщение: {user.message}"
    return {"status": "Пользователь добавлен", "user_id": next_index}


@app.put("/user/{user_id}/{username}/{age}")
async def user_update(user_id, mess):
    users[user_id] = mess
    return f"The user {user_id} is registered"


@app.delete("/user/{user_id}")
async def user_delete(user_id):
    users.pop(user_id)
