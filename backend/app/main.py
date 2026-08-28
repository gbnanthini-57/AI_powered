from fastapi import FastAPI
from backend.app.api import health, logs, incidents, analysis, verification, github

app = FastAPI()

app.include_router(health.router)
app.include_router(logs.router)
app.include_router(incidents.router)
app.include_router(analysis.router)
app.include_router(verification.router)
app.include_router(github.router)

@app.get("/")
def read_root():
    return {"message": "API Debugger backend is running"}