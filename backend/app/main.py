
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.db.database import get_db


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


@app.get("/health/database")
def database_health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "service": "opshub-api",
            "database": "connected",
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "database": "disconnected",
            },
        )
