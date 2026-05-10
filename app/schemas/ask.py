from pydantic import BaseModel

class AskRequest(BaseModel):
  question: str

class SourceResponse(BaseModel):
  filename: str
  chunk_index: int

class AskResponse(BaseModel):
  question: str
  answer: str
  sources: list[SourceResponse]

