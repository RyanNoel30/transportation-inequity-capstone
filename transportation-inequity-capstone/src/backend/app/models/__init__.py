"""Data models for the backend app.

Define Pydantic models or ORM models here.
"""

# Example placeholder
from pydantic import BaseModel

class CommuteStats(BaseModel):
    region: str
    avg_commute_time: float
    total_workers: int
    no_vehicle_workers: int
