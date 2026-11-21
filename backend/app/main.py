
from fastapi import FastAPI

app = FastAPI(
    title="OpsHub API",
    description="Cloud-native IT Operations Management Platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to OpsHub",
        "service": "OpsHub API",
        "version": "0.1.0",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "opshub-api",
    }
