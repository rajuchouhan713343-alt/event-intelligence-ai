from pydantic import BaseModel, HttpUrl
from typing import Optional


class SearchResult(BaseModel):
    title: str
    url: str
    snippet: Optional[str] = ""


class Company(BaseModel):
    name: str
    website: Optional[str] = None
    sector: Optional[str] = None
    source: Optional[str] = None
