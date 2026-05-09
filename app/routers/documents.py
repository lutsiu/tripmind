from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.document import DocumentResponse
from app.services.document_service import save_document

router = APIRouter(
  prefix="/trips/{trip_id}/documents",
  tags=["Documents"]
)

@router.post("", response_model=DocumentResponse)
def upload_document(trip_id: str, file: UploadFile = File(...)):
  try: 
    return save_document(trip_id=trip_id, file=file)
  except ValueError as e:
    raise HTTPException(status_code=404, detail=str(e))