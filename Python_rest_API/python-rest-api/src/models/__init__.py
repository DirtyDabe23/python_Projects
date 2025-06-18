from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str = None

class User(BaseModel):
    id: int
    username: str
    email: str

# You can add more models as needed for your API.