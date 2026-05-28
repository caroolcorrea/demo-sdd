"""
main.py — Entry point FastAPI.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.application.exceptions import ApplicationException

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("[STARTUP] demo-sdd starting...")
    yield
    logger.info("[SHUTDOWN] demo-sdd shutting down...")


app = FastAPI(
    title="demo-sdd",
    description="Demo project — Spec-Driven Design + Clean Architecture",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Exception handlers ---

@app.exception_handler(ApplicationException)
async def application_exception_handler(request: Request, exc: ApplicationException):
    logger.warning("[APP_ERROR] %s — %s", exc.code, exc.message)
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "error_code": exc.code, "message": exc.message},
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error("[UNHANDLED] %s", exc, exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"success": False, "error_code": "INTERNAL_ERROR", "message": "Internal server error"},
    )


# --- Routes ---

@app.get("/health", tags=["health"])
async def health():
    """Health check."""
    return {"status": "ok"}
