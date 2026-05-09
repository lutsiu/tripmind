from fastapi import APIRouter

from app.schemas.trip import CreateTripRequest, TripResponse
from app.services.trip_service import create_trip

router = APIRouter(
  prefix="/trips",
  tags=["Trips"]
)


@router.post("", response_model=TripResponse)
def create_trip_endpoint(request: CreateTripRequest):
  return create_trip(request.name)