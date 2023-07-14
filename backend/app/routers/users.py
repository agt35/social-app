from fastapi import APIRouter
import bcrypt

from app.database.database import *
from app.models.user import *

router = APIRouter()


@router.get("/")
async def get_users():
    users = await retrieve_users()
    return {"users": users}


@router.get("/{username}")
async def get_user(username: str):
    user = await retrieve_user(username)
    return user


@router.post("/")
async def create_user(user: User):
    existing_user = await retrieve_user(user.username)
    if existing_user:
        return {"error": "User already exists"}
    user = await user_collection.insert_one(user)
    return user


@router.post("/login")
async def login_user(user: User):
    user_in_db = await retrieve_user(user_in_db.username)
    if not user_in_db:
        return {"error": "User does not exist"}
    if not bcrypt.checkpw(user_in_db.password.encode(), user.password.encode()):
        return {"error": "Incorrect password"}
    return user_in_db
