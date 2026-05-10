from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.core.config import VECTOR_DB_DIR

def search_similar_chunks(
    trip_id: str,
    question: str,
    k: int = 3
):
  vector_store = Chroma(
    collection_name=f"trip_{trip_id}",
    persist_directory=str(VECTOR_DB_DIR),
    embedding_function=OpenAIEmbeddings(
            model="text-embedding-3-small"
        )
  )

  results = vector_store.similarity_search(
    query=question,
    k=k
  )

  return results