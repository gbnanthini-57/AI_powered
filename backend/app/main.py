from fastapi import FastAPI
from backend.app.api import health

app = FastAPI()

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"message": "API Debugger backend is running"}