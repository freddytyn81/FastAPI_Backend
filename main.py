from fastapi import FastAPI
from app.routers import user
import uvicorn


app = FastAPI()
app.include_router(user.router)

