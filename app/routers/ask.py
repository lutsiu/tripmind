from fastapi import APIRouter

from app.schemas.ask import AskRequest, AskResponse
from app.services.rag_service import ask_trip_documents

router = APIRouter(
    prefix="/ask",
    tags=["Ask"]
)


@router.post("/{trip_id}", response_model=AskResponse)
def ask_trip(
    trip_id: str,
    request: AskRequest
):
    return ask_trip_documents(
        trip_id=trip_id,
        question=request.question
    )