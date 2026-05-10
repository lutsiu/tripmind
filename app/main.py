from fastapi import FastAPI

from app.core.config import APP_NAME
from app.routers import trips, documents, ask

app = FastAPI(title=APP_NAME)

app.include_router(trips.router)
app.include_router(documents.router)
app.include_router(ask.router)


@app.get("/health")
def health_check():
  return {
    "status": "ok",
    "app": APP_NAME
  }

#  af4287da-0937-4f22-aebf-0a234a1293f3