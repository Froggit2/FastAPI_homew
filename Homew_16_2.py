from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/user")
async def users_list():
    return users




# @app.post("/user/{username}/{age}")
# async def user_add(username, age, message, user_id):
#     current_index = str(int(max(users, key=f"Имя: {username}, возраст: {age}")) + 1)
#     users[current_index] = message
#     return f"User {user_id} is registered."




@app.put("/user/{user_id}/{username}/{age}")
async def user_update(user_id, mess):
    users[user_id] = mess
    return f"The user {user_id} is registered"


@app.delete("/user/{user_id}")
async def user_delete(user_id):
    users.pop(user_id)