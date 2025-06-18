from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to the Python REST API!", "status": "success"}

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}

def setup_routes(app):
    app.include_router(router)