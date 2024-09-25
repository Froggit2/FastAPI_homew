from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}




@app.get("/user")
async def users_list():
    return users



@app.post("/user/{username}/{age}")
async def user_add(username, age):
    user_id = str(int(max(users.keys(), key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def user_update(user_id, username, age):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"


@app.delete("/user/{user_id}")
async def user_delete(user_id):
    users.pop(user_id)
    return f"User {user_id} has benn deleted!"