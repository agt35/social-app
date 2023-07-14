from fastapi import FastAPI

from app.routers.users import router as users_router

from app.database.database import init_db
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["https://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_database():
    await init_db()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}


app.include_router(users_router, prefix="/users", tags=["users"])
