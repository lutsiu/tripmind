from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from app.core.config import VECTOR_DB_DIR

def get_embbeddings(): 
  return OpenAIEmbeddings(
    model="text-embedding-3-small"
  )

def store_chunks(
    trip_id: str,
    filename: str,
    chunks: list[str]
) -> int:
  documents = []

  for index, chunk in enumerate(chunks):
    documents.append(
      Document(
        page_content=chunk,
        metadata={
          "trip_id": trip_id,
          "filename": filename,
          "chunk_index": index
        }
      )
    )

  vector_store=Chroma(
    collection_name=f"trip_{trip_id}",
    persist_directory=str(VECTOR_DB_DIR),
    embedding_function=get_embbeddings()
  )

  return len(documents)


