from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

ROOT_DIR = Path(__file__).parent.parent.parent

APP_NAME = os.getenv("APP_NAME", "TripMind")
ENV = os.getenv("ENV", "dev")

STORAGE_DIR = ROOT_DIR / "storage"
TRIP_STORAGE_DIR = STORAGE_DIR / "trips"

VECTOR_DB_DIR = STORAGE_DIR / "vector_db"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")