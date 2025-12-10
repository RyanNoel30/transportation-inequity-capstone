from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
def stats():
    """Placeholder endpoint for commute stats."""
    return {"message": "Commute stats placeholder"}
