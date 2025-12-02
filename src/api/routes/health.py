"""Health check routes for FKS Stocks Service"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse({
        "status": "healthy",
        "service": "fks_stocks",
        "timestamp": datetime.utcnow().isoformat()
    })
