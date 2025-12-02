"""
FKS Stocks Trading Service

This service provides:
- Stock market analysis (equity market analysis)
- Signal generation for stock trading
- Integration with fks-app, fks-execution, and fks-data
"""
import logging
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Import routes
try:
    from api.routes.health import router as health_router
except ImportError:
    logger.warning("Could not import health router")
    health_router = None

app = FastAPI(
    title="FKS Stocks Trading Service",
    description="Stock market analysis and signal generation for equity markets",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
if health_router:
    app.include_router(health_router, tags=["health"])


@app.on_event("startup")
async def startup_event():
    """Initialize service on startup"""
    logger.info("Starting FKS Stocks Trading Service...")
    logger.info("FKS Stocks Trading Service started successfully")


@app.get("/")
async def root():
    """Root endpoint"""
    return JSONResponse({
        "service": "fks_stocks",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "health": "/health"
        },
        "features": [
            "Stock market analysis",
            "Signal generation",
            "Integration with fks-app, fks-execution, fks-data"
        ]
    })


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("SERVICE_PORT", "8016"))
    uvicorn.run(app, host="0.0.0.0", port=port)
