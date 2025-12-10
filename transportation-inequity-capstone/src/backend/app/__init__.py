from fastapi import APIRouter

router = APIRouter()

# Import routes so they are registered
from .routes import commute  # noqa: F401

# Mount route(s)
router.include_router(commute.router, prefix="/commute")
