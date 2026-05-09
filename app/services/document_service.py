
from fastapi import UploadFile
from app.services.text_extraction_service import extract_text
from app.core.config import TRIP_STORAGE_DIR
from app.schemas.document import DocumentResponse

def save_document(trip_id: str, file: UploadFile) -> DocumentResponse:
  trip_dir = TRIP_STORAGE_DIR / trip_id

  if not trip_dir.exists():
    raise FileNotFoundError("Trip not found")
  
  documents_dir = trip_dir / "documents"
  documents_dir.mkdir(parents=True, exist_ok=True)

  file_path = documents_dir / file.filename

  with open(file_path, "wb") as buffer:
    buffer.write(file.file.read())

  extracted_text = extract_text(file_path=file_path)

  print("\n--- EXTRACTED TEXT PREVIEW ---")
  print(extracted_text[:1000])
  print("--- END PREVIEW ---\n")

  return DocumentResponse(
    filename=file.filename,
    path=str(file_path),
    message="Document uploaded successfully"
  )
