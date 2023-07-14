from beanie import Document, Insert, before_event
import bcrypt


class User(Document):
    username: str
    email: str
    password: str

    @before_event(Insert)
    async def hash_password(self):
        hashed = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt(10))
        self.password = hashed

    class Settings:
        name = "users"
