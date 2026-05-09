from fastapi import FastAPI

from app.core.config import APP_NAME
from app.routers import trips, documents

app = FastAPI(title=APP_NAME)

app.include_router(trips.router)
app.include_router(documents.router)

@app.get("/health")
def health_check():
  return {
    "status": "ok",
    "app": APP_NAME
  }