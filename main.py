# from fastapi import FastAPI
# from enum import Enum

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/")
# async def post():
#     return {"message": "Hello from POST"}

# @app.put("/")
# async def put():
#     return {"message": "Hello from PUT"}

# @app.get("/users")
# async def list_users():
#     return{"messages": "List of users"}
# @app.get("users/1")
# async def admin_user():
#     return {"message ": "this is the admin user"}

# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     return {"user_id":user_id}

from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_tables
from routes.tasks import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

@app.get("/")
def root():
    return {"message": "Task API is running"}

