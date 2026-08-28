from fastapi import FastAPI
from backend.app.api import health, logs, incidents

app = FastAPI()

app.include_router(health.router)
app.include_router(logs.router)
app.include_router(incidents.router)

@app.get("/")
def read_root():
    return {"message": "API Debugger backend is running"}