from pydantic import BaseModel

class DocumentResponse(BaseModel):
  filename: str
  path: str
  message: str 