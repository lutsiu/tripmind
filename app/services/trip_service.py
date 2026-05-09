from uuid import uuid4

from app.core.config import TRIP_STORAGE_DIR
from app.schemas.trip import TripResponse

def create_trip(name: str) -> TripResponse:
  trip_id = str(uuid4())

  trip_dir = TRIP_STORAGE_DIR / trip_id
  trip_dir.mkdir(parents=True, exist_ok=True)

  return TripResponse(
    id=trip_id, name=name
  )