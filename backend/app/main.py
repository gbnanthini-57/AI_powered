from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api import health, logs, incidents, analysis, verification, github

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(logs.router)
app.include_router(incidents.router)
app.include_router(analysis.router)
app.include_router(verification.router)
app.include_router(github.router)

@app.get("/")
def read_root():
    return {"message": "API Debugger backend is running"}