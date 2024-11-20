from fastapi import FastAPI
from dummy import users
app = FastAPI()
@app.get("/")
def read_root():
    return{"Hello" : "World"};

@app.get("/users")
def get_all_users():
    return{
        "data": users
}

@app.get("/users/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user["id"]==user_id:
            return{
                "data": user
        }

@app.post("/users")
def create_user(user: dict):
    user_count=len(users)
    new_user= {
        "id":user_count + 1,
        "name":user["name"],
        "email":user["email"]
    }
    users.append(new_user)
    return{ "data": user}

