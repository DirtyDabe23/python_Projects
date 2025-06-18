from fastapi import FastAPI
from api.routes import setup_routes

app = FastAPI()

setup_routes(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)