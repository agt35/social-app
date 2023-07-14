from beanie import init_beanie

from app.models.user import User
import os

import motor.motor_asyncio

username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")

user_collection = User


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        f"mongodb://{username}:{password}@mongodb:27017/social-app?authSource=admin"
    )
    await init_beanie(database=client["social-app"], document_models=[User])


async def retrieve_users() -> list[User]:
    users = await user_collection.find().to_list()
    print(users)
    return users


async def retrieve_user(username: str) -> User:
    user = await user_collection.find_one({"username": username})
    return user


async def create_user(user: User) -> User:
    user = await user_collection.insert_one(user)
    return user
