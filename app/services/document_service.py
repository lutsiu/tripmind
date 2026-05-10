
from fastapi import UploadFile
from app.services.text_extraction_service import extract_text
from app.core.config import TRIP_STORAGE_DIR
from app.schemas.document import DocumentResponse
from app.services.chunking_service import chunk_text
from app.services.vector_store_service import store_chunks

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
  chunks = chunk_text(extracted_text)

  stored_chunks_count = store_chunks(
    trip_id=trip_id, 
    filename=file.filename, 
    chunks=chunks
  )

  print(f"Stored chunks in vector DB: {stored_chunks_count}")

  return DocumentResponse(
    filename=file.filename,
    path=str(file_path),
    message=f"Document uploaded, extracted, chunked, and indexed. Chunks: {stored_chunks_count}"
  )

# af4287da-0937-4f22-aebf-0a234a1293f3