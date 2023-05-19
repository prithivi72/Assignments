from fastapi import FastAPI
import uvicorn
from scripts.core.services.course_service import app_router

app_main = FastAPI()

app_main.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run("main:app_main")
