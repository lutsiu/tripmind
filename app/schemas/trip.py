from pydantic import BaseModel

class CreateTripRequest(BaseModel):
  name: str

class TripResponse(BaseModel):
  id: str
  name: str

  