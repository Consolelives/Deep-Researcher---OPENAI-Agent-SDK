from pydantic import BaseModel

class SearchResult(BaseModel):
    tilte: str
    url: str
    summary: str 