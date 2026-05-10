from fastapi import APIRouter

from app.schemas.ask import AskRequest

from app.services.retrieval_service import search_similar_chunks

router = APIRouter(
  prefix="/ask",
  tags=["Ask"]
)

@router.post("/{trip_id}")
def ask_trip(
  trip_id: str,
  request: AskRequest
):
  results = search_similar_chunks(
    trip_id=trip_id, question=request.question
  )

  return {
        "question": request.question,
        "chunks": [
            result.page_content
            for result in results
        ]
  }